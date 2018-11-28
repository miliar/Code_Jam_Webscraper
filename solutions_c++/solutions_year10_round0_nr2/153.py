// the big num class is from internet


#include <stdio.h>
#include <string.h>
#include <iostream>
#include "Integer.h"

Integer ZERO(0);
Integer ONE(1);

template <typename T>
T gcd(T a,T b)
{
	T c;
	while(1)
	{
		c = a%b;
		if(c==0)
			return b;
		a = b;
		b = c;
	}
}

Integer gcdInteger(Integer &a, Integer &b)
{
	Integer c;
	while(1)
	{
		Integer::Mod(a,b,c);
		//c = a%b;
		if(c==ZERO)
			return b;
		a = b;
		b = c;
	}
}
//////////////////////////////////////////////////////////////////////////
// quick sort in non-recursive mode
//////////////////////////////////////////////////////////////////////////
template <typename T>
void quick_sort_nonR(T *base, int num)
{
	T *lo, *hi;              /* ends of sub-array currently sorting */
	T *mid;                  /* points to middle of subarray */
	T *loguy, *higuy;        /* traveling pointers for partition step */
	size_t size;                /* size of the sub-array */
	T *lostk[32], *histk[32];
	int stkptr;                 /* stack for saving sub-array to be processed */

	int width = sizeof(T);
	if (num < 2)
		return;                 /* nothing to do */

	stkptr = 0;                 /* initialize stack */

	lo = (T *)base;
	hi = (T *)base +(num-1);        /* initialize limits */

	/* this entry point is for pseudo-recursion calling: setting
	lo and hi and jumping to here is like recursion, but stkptr is
	preserved, locals aren't, so we preserve stuff on the stack */
recurse:

	size = (hi - lo) + 1;        /* number of el's to sort */

	/* below a certain size, it is faster to use a O(n^2) sorting method */
	if (size <= 8) {
		short_sort(lo, hi);
	}
	else {
		/* First we pick a partitioning element.  The efficiency of the
		algorithm demands that we find one that is approximately the median
		of the values, but also that we select one fast.  We choose the
		median of the first, middle, and last elements, to avoid bad
		performance in the face of already sorted data, or data that is made
		up of multiple sorted runs appended together.  Testing shows that a
		median-of-three algorithm provides better performance than simply
		picking the middle element for the latter case. */

		mid = lo + (size / 2);      /* find middle element */

		/* Sort the first, middle, last elements into order */
		if ( *lo > *mid) {
			//            swap(lo, mid, width);
			T temp = *lo;
			*lo = *mid;
			*mid = temp;
		}
		if (*lo>*hi){
			//            swap(lo, hi, width);
			T temp = *lo;
			*lo = *hi;
			*hi = temp;
		}
		if (*mid>*hi) {
			//            swap(mid, hi, width);
			T temp = *mid;
			*mid = *hi;
			*hi = temp;
		}

		/* We now wish to partition the array into three pieces, one consisting
		of elements <= partition element, one of elements equal to the
		partition element, and one of elements > than it.  This is done
		below; comments indicate conditions established at every step. */

		loguy = lo;
		higuy = hi;

		/* Note that higuy decreases and loguy increases on every iteration,
		so loop must terminate. */
		for (;;) 
		{
			/* lo <= loguy < hi, lo < higuy <= hi,
			A[i] <= A[mid] for lo <= i <= loguy,
			A[i] > A[mid] for higuy <= i < hi,
			A[hi] >= A[mid] */

			/* The doubled loop is to avoid calling comp(mid,mid), since some
			existing comparison funcs don't work when passed the same
			value for both pointers. */

			if (mid > loguy) {
				do  {
					loguy += 1;
				} while (loguy < mid && *loguy<=*mid);
			}
			if (mid <= loguy) {
				do  {
					loguy += 1;
				} while (loguy <= hi && *loguy<=*mid);
			}

			/* lo < loguy <= hi+1, A[i] <= A[mid] for lo <= i < loguy,
			either loguy > hi or A[loguy] > A[mid] */

			do  {
				higuy -= 1;
			} while (higuy > mid && *higuy>*mid);

			/* lo <= higuy < hi, A[i] > A[mid] for higuy < i < hi,
			either higuy == lo or A[higuy] <= A[mid] */

			if (higuy < loguy)
				break;

			/* if loguy > hi or higuy == lo, then we would have exited, so
			A[loguy] > A[mid], A[higuy] <= A[mid],
			loguy <= hi, higuy > lo */

			//            swap(loguy, higuy, width);
			{
				T temp = *loguy;
				*loguy = *higuy;
				*higuy = temp;
			}

			/* If the partition element was moved, follow it.  Only need
			to check for mid == higuy, since before the swap,
			A[loguy] > A[mid] implies loguy != mid. */

			if (mid == higuy)
				mid = loguy;

			/* A[loguy] <= A[mid], A[higuy] > A[mid]; so condition at top
			of loop is re-established */
		}

		/*     A[i] <= A[mid] for lo <= i < loguy,
		A[i] > A[mid] for higuy < i < hi,
		A[hi] >= A[mid]
		higuy < loguy
		implying:
		higuy == loguy-1
		or higuy == hi - 1, loguy == hi + 1, A[hi] == A[mid] */

		/* Find adjacent elements equal to the partition element.  The
		doubled loop is to avoid calling comp(mid,mid), since some
		existing comparison funcs don't work when passed the same value
		for both pointers. */

		higuy += 1;
		if (mid < higuy) {
			do  {
				higuy -= 1;
			} while (higuy > mid && *higuy==*mid);
		}
		if (mid >= higuy) {
			do  {
				higuy -= 1;
			} while (higuy > lo && *higuy==*mid);
		}

		/* OK, now we have the following:
		higuy < loguy
		lo <= higuy <= hi
		A[i]  <= A[mid] for lo <= i <= higuy
		A[i]  == A[mid] for higuy < i < loguy
		A[i]  >  A[mid] for loguy <= i < hi
		A[hi] >= A[mid] */

		/* We've finished the partition, now we want to sort the subarrays
		[lo, higuy] and [loguy, hi].
		We do the smaller one first to minimize stack usage.
		We only sort arrays of length 2 or more.*/

		if ( higuy - lo >= hi - loguy ) {
			if (lo < higuy) {
				lostk[stkptr] = lo;
				histk[stkptr] = higuy;
				++stkptr;
			}                           /* save big recursion for later */

			if (loguy < hi) {
				lo = loguy;
				goto recurse;           /* do small recursion */
			}
		}
		else {
			if (loguy < hi) {
				lostk[stkptr] = loguy;
				histk[stkptr] = hi;
				++stkptr;               /* save big recursion for later */
			}

			if (lo < higuy) {
				hi = higuy;
				goto recurse;           /* do small recursion */
			}
		}
	}

	/* We have sorted the array, except for any pending sorts on the stack.
	Check if there are any, and do them. */

	--stkptr;
	if (stkptr >= 0) {
		lo = lostk[stkptr];
		hi = histk[stkptr];
		goto recurse;           /* pop subarray from stack */
	}
	else
		return;                 /* all subarrays done */
}

template <typename T>
void short_sort (T *lo, T *hi)
{
	T *p, *max;
	int width = sizeof(T);
	/* Note: in assertions below, i and j are alway inside original bound of
	array to sort. */

	while (hi > lo) {
		/* A[i] <= A[j] for i <= j, j > hi */
		max = lo;
		for (p = lo+1; p <= hi; p += 1) {
			/* A[i] <= A[max] for lo <= i < p */
			if ( *p> *max) {
				max = p;
			}
			/* A[i] <= A[max] for lo <= i <= p */
		}

		/* A[i] <= A[max] for lo <= i <= hi */

		//        swap(max, hi, width);
		T temp = *max;
		*max = *hi;
		*hi = temp;

		/* A[i] <= A[hi] for i <= hi, so A[i] <= A[j] for i <= j, j >= hi */

		hi -= 1;

		/* A[i] <= A[j] for i <= j, j > hi, loop top condition established */
	}
	/* A[i] <= A[j] for i <= j, j > lo, which implies A[i] <= A[j] for i < j,
	so array is sorted */
}
//unsigned int TIMEARRAY[1000] = {0};
//unsigned int DIFARRAY[1000] = {0};
Integer bigTIMEARRAY[1000];
Integer bigDIFARRAY[1000];

int main(int argc, char* argv[])
{
	FILE *pIn = fopen("C:\\jam\\B-large.in", "r");
	FILE *pOt = fopen("C:\\jam\\B-large.ot", "w");

	int caseNum = 0;

	fscanf(pIn, "%d", &caseNum);

	for(int i = 0 ; i < caseNum ; i++)
	{
		int EVNETN = 0;
		fscanf(pIn, "%d", &EVNETN);

		char tmpBigNum[60] = {0};
		for(int n = 0 ; n < EVNETN ; n++)
		{
			fscanf(pIn, "%s", &tmpBigNum[0]);
			Integer tmp(&tmpBigNum[0], 10);
			bigTIMEARRAY[n] = tmp;
		}
		
		quick_sort_nonR(&bigTIMEARRAY[0], EVNETN);

		Integer base = bigTIMEARRAY[0];
		for(int n = 0 ; n <EVNETN ; n++)
		{
//			bigDIFARRAY[n] = bigTIMEARRAY[n] - base;
			Integer::Sub(bigTIMEARRAY[n], base, bigDIFARRAY[n] );
		}

		Integer g = bigDIFARRAY[1];
		for(int n = 1 ; n < EVNETN ; n++)
		{
			if(bigDIFARRAY[n] != ZERO)
				g = gcdInteger(g, bigDIFARRAY[n]);
		}

		Integer y(0);
		Integer target(0);

		if(g == ONE)
		{
			y = 0;
		}
		else
		{
			Integer reminder;
			Integer::Mod(base, g, reminder);
			if( reminder==ZERO )
			{
				//0
				y = 0;
			}
			else
			{
				Integer quo;
				Integer::Div(base, g, quo, reminder);
				Integer::Add(quo, Integer(1), y);
				Integer::Mul(y, g, y);
				Integer::Sub(y, base, y);

//				y = (base / g + 1 )*g - base;
			}

		}
		

		// out
		char answer[60] ={0};
		y.ToString(&answer[0], 10);
		fprintf(pOt, "Case #%d: %s\n", i+1 , answer);

	}
	fclose(pOt);
	fclose(pIn);

	return 0;
}



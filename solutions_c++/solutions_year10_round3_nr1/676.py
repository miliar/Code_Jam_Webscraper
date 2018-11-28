#include <stdio.h>

inline int Parent (int i)
{
	return (i-1)>>1;
}

inline int Left (int i)
{
	return ((i+1)<<1)-1;
}

inline int Right (int i)
{
	return (i+1)<<1;
}

inline void swap(unsigned int &a, unsigned int &b)
{
	unsigned int c = a; 
	a = b;
	b = c;
}

void Heapify(unsigned int* A, unsigned int* B, int Index, int Size)
{
	int LeftInd;
	int RightInd;
	while (Left(Index) < Size)
	{
		LeftInd = Left(Index);
		RightInd = Right(Index);

		int MaxPos = LeftInd;
		
		if ((RightInd<Size) && (A[RightInd]>A[LeftInd]))
			MaxPos = RightInd;

		if (A[Index]<A[MaxPos])
		{
			swap(A[Index], A[MaxPos]);
			swap(B[Index], B[MaxPos]);
			Index = MaxPos;
		}
		else
			break;
	}
}

void BuildHeap(unsigned int* A, unsigned int* B, int Size)
{
	for (int i=Size/2; i>=0; i--)
	{
		Heapify(A, B, i, Size);
	}
}

void HeapSort(unsigned int* A, unsigned int* B, int Size)
{
	BuildHeap(A, B, Size);
	for (int i=1; i<Size; i++)
	{
		swap(A[0], A[Size-i]);
		swap(B[0], B[Size-i]);
		Heapify(A, B, 0, Size-i);
	}
}


void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "a+");

	int NumCase;
	fscanf(InStream, "%d", &NumCase);

	for (int Case = 1; Case<=NumCase; Case++)
	{
		unsigned long int result = 0;
		int N;
		fscanf(InStream, "%d", &N);
		unsigned int *A = new unsigned int [N];
		unsigned int *B = new unsigned int [N];

		for (int i=0; i<N; i++)
			fscanf(InStream, "%d %d", &A[i], &B[i]);

		/*for (int i=0; i<N; i++)
			printf("%d - %d\n", A[i], B[i]);
		printf("\n");*/
		
		HeapSort(A, B, N);

		/*for (int i=0; i<N; i++)
			printf("%d - %d\n", A[i], B[i]);
		printf("\n");*/

		for (int i=0; i<N-1; i++)
		{
			for (int j=i+1; j<N; j++)
			{
				if (B[i]>B[j])
					result++;
			}
		}
		
		fprintf(OutStream, "Case #%d: %d\n", Case, result);
		delete [] A;
		delete [] B;
	}

	fclose(InStream);
	fclose(OutStream);
}

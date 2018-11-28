#include <cstdio>
#include <cstdlib>

int cmp(const void *a, const void *b)
{
  if (*((int*)a)<*((int*)b))
    return -1;
  else if (*((int*)a)>*((int*)b))
    return 1;
  else return 0;
}

int min4(int a, int b, int c, int d)
{
  if (a<=b && a<=c && a<=d)
    return a;
  else if (b<=a && b<=c && b<=d)
    return b;
  else if (c<=a && c<=b && c<=d)
    return c;
  else
    return d;
}

int main()
{
  int N;
  int NA, NB, T;
  int depA[101], depB[101], arrA[101], arrB[101]; //train departing from A at depA[i] arrives at B at arrA[i] !!!
  int avaA, avaB;
  int needA, needB;
  scanf("%d\n",&N);

  for (int n=0; n<N; n++)
    {
      printf("Case #%d: ",n+1);
      needA=0;
      needB=0;

      scanf("%d\n %d %d\n",&T, &NA, &NB);

      int hour, min;
      for (int i=0; i<NA; i++)
	{
	  scanf("%d:%d ", &hour, &min);
	  depA[i]=hour*60+min;
	  scanf("%d:%d\n", &hour, &min);
	  arrA[i]=hour*60+min;
	  arrA[i]+=T;
	}
      arrA[NA]=depA[NA]=26*60;
      for (int i=0; i<NB; i++)
	{
	  scanf("%d:%d ", &hour, &min);
	  depB[i]=hour*60+min;
	  scanf("%d:%d\n", &hour, &min);
	  arrB[i]=hour*60+min;
	  arrB[i]+=T;
	}
      arrB[NB]=depB[NB]=26*60;

      avaA=0;
      avaB=0;

      qsort(depA, NA, sizeof(int), &cmp);
      qsort(arrA, NA, sizeof(int), &cmp);
      qsort(depB, NB, sizeof(int), &cmp);
      qsort(arrB, NB, sizeof(int), &cmp);
      
      int i_depA, i_arrA, i_depB, i_arrB;
      i_depA=i_arrA=i_depB=i_arrB=0;

      while (!(i_depA == NA && i_arrA == NA && i_depB == NB && i_arrB == NB))
	{
	  //	  printf("%d %d %d %d\n",i_depA,i_arrA,i_depB,i_arrB);
	  if (arrA[i_arrA]<=min4(arrA[i_arrA], arrB[i_arrB], depA[i_depA], depB[i_depB]))
	    {
	      avaB++;
	      i_arrA++;
	    }
	  else if (arrB[i_arrB]<=min4(arrA[i_arrA], arrB[i_arrB], depA[i_depA], depB[i_depB]))
	    {
	      avaA++;
	      i_arrB++;
	    }
	  else if (depA[i_depA]<=min4(arrA[i_arrA], arrB[i_arrB], depA[i_depA], depB[i_depB]))
	    {
	      if (avaA>0)
		avaA--;
	      else
		needA++;

	      i_depA++;
	    }
	  else
	    {
	      if (avaB>0)
		avaB--;
	      else
		needB++;

	      i_depB++;
	    }
	}


      printf("%d %d\n", needA, needB);
    }

  return 0;
}

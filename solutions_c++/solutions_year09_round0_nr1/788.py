#include <cstdio>
#include <cstring>

int main()
{
  int L,D,N;
  scanf("%d %d %d\n",&L,&D,&N);

  char *dictionary=new char[D*(L+1)];

  for (int i=0; i<D; i++)
    {
      scanf("%s\n",dictionary+i*(L+1));
    }


  int *pattern=new int[L*26];
  char c;
  int ret;

  for (int i=0; i<N; i++)
    {
      ret=0;
      memset(pattern,0,L*26*sizeof(int));
      for (int j=0; j<L; j++)
	{
	  scanf(" %c ",&c);
	  if (c=='(')
	    {
	      while (true)
		{
		  scanf(" %c ",&c);
		  if (c==')')
		    break;

		  pattern[j*26+c-'a']=1;
		}
	    }
	  else
	    pattern[j*26+c-'a']=1;
	}

      for (int j=0; j<D; j++)
	{
	  for (int k=0; k<L; k++)
	    {
	      if (!pattern[k*26+dictionary[j*(L+1)+k]-'a'])
		break;

	      if (k==L-1)
		ret++;
	    }
	}

      printf("Case #%d: %d\n",i+1,ret);
    }



  delete[] dictionary;
  delete[] pattern;
  return 0;
}

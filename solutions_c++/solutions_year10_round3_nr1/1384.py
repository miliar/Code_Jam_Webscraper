#include <iostream> //Header untuk stream input dan output pada bahasa C++
#include <iomanip>  //Header untuk manipulasi tampilan output
#include <string>    //Header untuk standard C++ math library

using namespace std;

int main()
{	struct array{
		long INT;
	};

	array ANS[1000];
	array A[1000];
	array B[1000];


    int T=0,N=0;
	long hitung;
	int pointer;

	FILE*  OP=NULL;
	OP=fopen("A-large.in", "r");
	if(OP!=NULL)
	{   //cout<<"B-small.in found\n";
	}
    fscanf (OP, "%i", &T);

    for(int i=0;i<T;i++)
    {   N=0;
        fscanf (OP, "%i", &N);
        //printf("R = %i  K = %i  N =  %i\n",R,K,N);

        for(int j=0;j<N;j++)
        {   A[j].INT=0;
            fscanf (OP, "%i", &A[j].INT);
            fscanf (OP, "%i", &B[j].INT);
            //printf("G[%i] = %i  \n",j+1,G[j].INT);
        }
        hitung=0;

        for (int j=0;j<N;j++)
        {
            for(int k=j+1;k<N;k++)
            {   //printf("G[%i]=== A[j] = %i & B[j] = %i \n",j+1,A[j].INT,B[j].INT);
                //printf("G[%i]=== A[K] = %i & B[K] = %i \n",j+1,A[k].INT,B[k].INT);

                if((A[j].INT<A[k].INT)&&(B[j].INT>B[k].INT))
                {   hitung++;
                //out<<"if1";
                }
                else if((A[j].INT>A[k].INT)&&(B[j].INT<B[k].INT))
                {   hitung++;
                //cout<<"if2";
                }
                //cout<<"else";

            }

        }
        //cout<<"\n";
        ANS[i].INT=hitung;
        //printf("G[%i] = %i  \n",i+1,ANS[i].INT);
    }

    FILE* OC=fopen("A-Large.out", "w");

    for(int l=0;l<T;l++)
    {   fprintf (OC, "Case #%i: %i\n",l+1,ANS[l].INT);
        //printf ("Case #%i: %i\n",l+1,ANS[l].INT);
    }

    if(OP!=NULL)
    {   fclose(OP);
    }

    return 0;
}

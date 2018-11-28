#include <iostream> //Header untuk stream input dan output pada bahasa C++
#include <iomanip>  //Header untuk manipulasi tampilan output
#include <string>    //Header untuk standard C++ math library

using namespace std;

int main()
{	struct array{
		int INT;
	};

	array ANS[10000];
	array G[10];


    int T=0,R=0,K=0,N=0;
	int ON;
	int pointer;

	FILE*  OP=NULL;
	OP=fopen("C-small.in", "r");
	if(OP!=NULL)
	{   //cout<<"B-small.in found\n";
	}
    fscanf (OP, "%i", &T);

    for(int i=0;i<T;i++)
    {   K=0;
        N=0;
        pointer=0;
        fscanf (OP, "%i", &R);
        fscanf (OP, "%i", &K);
        fscanf (OP, "%i", &N);
        //printf("R = %i  K = %i  N =  %i\n",R,K,N);

        for(int j=0;j<N;j++)
        {   G[j].INT=0;
            fscanf (OP, "%i", &G[j].INT);
            //printf("G[%i] = %i  \n",j+1,G[j].INT);
        }

        int storage;
        int EURO=0;
        for (int k=0;k<R;k++)
        {   storage=0;
            int in=0;
            while(((storage+G[pointer].INT)<=K)&&(in<N)&&(pointer<N))
            {   storage=storage+G[pointer].INT;
                pointer++;
                if(pointer>=N)
                {   pointer=0;
                }
                in++;
                //cout<<"in +"<<in<<" ";
            }
            //cout<<""<<storage<<"  \n";
            EURO=EURO+storage;
        }
        //cout<<"\n";
        ANS[i].INT=EURO;
    }

    FILE* OC=fopen("C-small.out", "w");

    for(int l=0;l<T;l++)
    {   fprintf (OC, "Case #%i: %i\n",l+1,ANS[l].INT);
        //printf ("Case #%i: %i\n",l+1,ANS[l].INT);
    }

    if(OP!=NULL)
    {   fclose(OP);
    }

    return 0;
}

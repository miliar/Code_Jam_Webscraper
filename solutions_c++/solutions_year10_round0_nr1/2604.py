#include <iostream> //Header untuk stream input dan output pada bahasa C++
#include <iomanip>  //Header untuk manipulasi tampilan output
#include <string>    //Header untuk standard C++ math library

using namespace std;

int main()
{	struct array{
		int ANSWER;
	};

	array ANS[10000];

    int N=0,X=0;
    long int K=0;
	int SnapON;
	int ON;

	FILE*  OP=NULL;
	OP=fopen("A-Large.in", "r");
	if(OP==NULL)
	{   //fclose(OP);
        cin>>X;
        //cout<<X<<"\n";
    }
    if(OP!=NULL)
    {   fscanf (OP, "%i", &X);
    }

    for(int i=0;i<X;i++)
    {   N=0;
        K=0;
        SnapON=1;
        if(OP==NULL)
        {   cin>>N;
            cin>>K;
        }
        else
        {   fscanf (OP, "%i", &N);
            fscanf (OP, "%li", &K);
        }

        //cout<<N<<" = N "<<K<<" = K \n";
        ON=0;

            for(int j=1;j<N;j++)
            {   SnapON=2*SnapON+1;
            }

        //cout<<SnapON<<"= SnapON \n";

        if(N<1)
        {   ON=0;
        }
        else if (K==0)
        {   ON=0;
        }
        else if ((N==1)&&(K==1))
        {   ON=1;
        }
        else if (K==SnapON)
        {   ON=1;
            //cout<<"K==SnapON\n";
        }
        else if(K>SnapON)
        {   //cout<<"K>SnapON\n";
            while(K>SnapON)
            {   K=K-SnapON-1;
                //cout<<"K= "<<K<<"\n";
            }

            if (K==SnapON)
            {   ON=1;
            }
            else
            {   ON=0;
            }
        }
        else
        {   //cout<<"K<SnapON\n";
            ON=0;
        }
        ANS[i].ANSWER=ON;
    }
    FILE* OC=fopen("A-Large.out", "w");
    if (OC!= NULL)
    {   for(int k=0;k<X;k++)
        {   if (ANS[k].ANSWER==1)
            {   fprintf (OC, "Case #%i: ON\n",k+1);

            }
            else
            {   fprintf (OC, "Case #%i: OFF\n",k+1);
            }
        }
    }
    else
    {   for(int k=0;k<X;k++)
        {   if (ANS[k].ANSWER==1)
            {   cout<<"Case #"<<k+1<<": ON\n";
            }
            else
            {   cout<<"Case #"<<k+1<<": OFF\n";
            }
        }
    }


    if(OP!=NULL)
    {   fclose(OP);
    }

    return 0;
}

#include <iostream>
#include <string.h>
#include <stdio.h>


int searchNflag(char SE[100][100],int SE_flag[100],int S_no,char query[100])
    {
    for (int i=0;i<S_no;i++)
        {
        if (!strcmp(SE[i],query))
            {SE_flag[i]=0;break;}
        }
    int flag_count=0;

    for (int i=0;i<S_no;i++)
           flag_count+=SE_flag[i];

    return flag_count;
    }

int resetFlag(int SE_flag[100],int S_no)
    {
    for (int k=0;k<S_no;k++)
        SE_flag[k]=1;
    }


int main()
{
	int N;  //no of cases
	int S[20];	//no of search engines
	int Q[20];	//no of queries

    char se[20][100][100];
    char q[20][1000][100];

	cin>>N;
    //----take input---
	for(int i=0;i<N;i++)
		{
		cin>>S[i];

		for (int j=0;j<S[i];j++)
           gets(se[i][j]);

        cin>>Q[i];

        for(int k=0;k<Q[i];k++)
            gets(q[i][k]);
        }

     for (int i=0;i<N;i++)
        {
        //------------------------main logic---------------------
        int shift=0;
        int se_flag[100];
        resetFlag(se_flag,S[i]);

        for (int k=0;k<Q[i];k++)
            {
            //int searchNflag(char SE[100][100],int SE_flag[100],int S_no,char query[100])
            if (searchNflag(se[i],se_flag,S[i],q[i][k])==0)
                    {
                    shift++;
                    resetFlag(se_flag,S[i]);
                    k--;
                    }
             }
         cout<<"Case #"<<i+1<<": "<<shift<<endl;
         //----------------------------- main logic ends here----------
        }

      //cin>>N;
      return 0;
    }

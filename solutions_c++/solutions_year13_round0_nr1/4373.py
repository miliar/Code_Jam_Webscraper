#include<iostream>

using namespace std;
int main()
{
	int testcases,i,j, Xcount, Tcount, Ocount, dotcount;
	int winner ;
	char t[4][4], temp[10];
	cin>>testcases;
	//cin>>temp;
    int total = testcases;
	while(testcases--)
	{
		for(i=0;i<4;i++)
		{
		    cin>>temp;
		    for(j=0;j<4;j++)
		    {
		        t[i][j] = temp[j];
		    }
		}
		winner = 0;
		dotcount = 0;
		for(i=0;!winner && i<4;i++)
        {
            Xcount=0; Tcount=0; Ocount=0;
            for(j=0;j<4;j++)
            {
                if(t[i][j]=='X') Xcount++;
                else if (t[i][j]=='O') Ocount++;
                else if (t[i][j]=='T') Tcount = 1;
                else if(t[i][j]=='.'){ dotcount++; break; }
            }
            if((Xcount==3 && Tcount ==1) || Xcount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": X won\n";
            }
            if((Ocount==3 && Tcount ==1) || Ocount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": O won\n";
            }
        }
        //dotcount = 0;
        for(i=0;!winner && i<4;i++)
        {
            Xcount=0; Tcount=0; Ocount=0;
            for(j=0;j<4;j++)
            {
                if(t[j][i]=='X') Xcount++;
                else if (t[j][i]=='O') Ocount++;
                else if (t[j][i]=='T') Tcount = 1;
                else if(t[i][j]=='.') { dotcount++; break; }
            }
            if((Xcount==3 && Tcount ==1) || Xcount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": X won\n";
            }
            if((Ocount==3 && Tcount ==1) || Ocount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": O won\n";
            }
        }
        //dotcount = 0;
        if(!winner)
        {
            Xcount=0; Tcount=0; Ocount=0;
            for(j=0;j<4;j++)
            {
                if(t[j][j]=='X') Xcount++;
                else if (t[j][j]=='O') Ocount++;
                else if (t[j][j]=='T') Tcount = 1;
                else if(t[j][j]=='.') { dotcount++; }
            }
            if((Xcount==3 && Tcount ==1) || Xcount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": X won\n";
            }
            if((Ocount==3 && Tcount ==1) || Ocount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": O won\n";
            }
        }
        if(!winner)
        {
            Xcount=0; Tcount=0; Ocount=0;
            for(j=0;j<4;j++)
            {
                if(t[j][4-j-1]=='X') Xcount++;
                else if (t[j][4-j-1]=='O') Ocount++;
                else if (t[j][4-j-1]=='T') Tcount = 1;
                else if(t[j][4-j-1]=='.') { dotcount++; }
            }
            if((Xcount==3 && Tcount ==1) || Xcount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": X won\n";
            }
            if((Ocount==3 && Tcount ==1) || Ocount ==4)
            {
                winner = 1;
                cout<<"Case #"<<(total-testcases)<<": O won\n";
            }
        }
        //cout<<dotcount<<" "<<Xcount<<" "<<Ocount<<" "<<Tcount;
        if(!winner && dotcount>0)
        {
            cout<<"Case #"<<(total-testcases)<<": Game has not completed\n";
        }
        else if(!winner && dotcount==0)
        {
            cout<<"Case #"<<(total-testcases)<<": Draw\n";
        }
		/*for(i=0;i<4;i++)
		{
		    for(j=0;j<4;j++)
		    {
		        cout<<t[i][j];
		    }
		    cout<<"\n";
		}*/
	}
	return 0;
}

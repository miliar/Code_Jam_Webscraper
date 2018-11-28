#include <iostream>
#include <fstream>
using namespace std;

/*

3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/

int main()
{
    ifstream a("al.in");
    ofstream b("bl.out");
    #define cin a
    #define cout b
    int t;
    cin>>t;
    for(int tt=0; tt<t; tt++)
    {
        int res=0;

        int posO = 1;
        int posB = 1;
        int taskO = -1;
        int taskB = -1;
        int but[100]={0};
        char col[100]={0};


        int n;
        cin>>n;
        for(int i=0; i<n; i++)
        {
            char c; int b;
            cin>>c>>b;
            but[i] = b;
            col[i] = c;
        }


        int at = 0;

        while(at<n)
        {
            for(int i=at; i<=n&&(taskB==-1 || taskO==-1); i++)
            {
                if( taskB==-1 && col[i]=='B' ) taskB = but[i];
                if( taskO==-1 && col[i]=='O' ) taskO = but[i];
            }

            bool pushed = 0;
            // blue
            if( posB > taskB ) posB--;
            else if( posB < taskB ) posB++;
            else if( col[at]=='B' )
            {
                pushed = 1;
                taskB = -1;
                at++;
            }

            // orange
            if( posO > taskO ) posO--;
            else if( posO < taskO ) posO++;
            else if( col[at]=='O' && !pushed)
            {
                taskO = -1;
                at++;
            }

            //cout<<"orange at "<<posO<<", blue at "<<posB<<endl;

            res++;
        }

        cout<<"Case #"<<tt+1<<": "<<res<<endl;
    }
}

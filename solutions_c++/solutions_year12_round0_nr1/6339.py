#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<map>
#include<cmath>
#include<sstream>
#include <deque>
#define mx 100010
using namespace std;
//int dx[]= {0,0,-1,1};
//int dy[]= {1,-1,0,0};
//int dx[]= {-1,1,-2,2,-2,2,-1,1};
//int dy[]= {-2,-2,-1,-1,1,1,2,2};
main()
{
    int test,t=0;
    scanf("%d",&test);
    cin.ignore();
    while(test--)
    {
        string a;
        getline(cin,a);
        int sz=a.size();
        printf("Case #%d: ",++t);

        for(int i=0; i<sz; i++)
        {
            if(a[i]>='a' && a[i]<='z')
            {
                if(a[i]=='a')
                    cout<<'y';

                else if(a[i]=='b')
                    cout<<'h';

                else if(a[i]=='c')
                    cout<<'e';

                else if(a[i]=='d')
                    cout<<'s';

                else if(a[i]=='e')
                    cout<<'o';

                else if(a[i]=='f')
                    cout<<'c';

                else if(a[i]=='g')
                    cout<<'v';

                else if(a[i]=='h')
                    cout<<'x';

                else if(a[i]=='i')
                    cout<<'d';

                else if(a[i]=='j')
                    cout<<'u';

                else if(a[i]=='k')
                    cout<<'i';

                else if(a[i]=='l')
                    cout<<'g';

                else if(a[i]=='m')
                    cout<<'l';

                else if(a[i]=='n')
                    cout<<'b';

                else if(a[i]=='o')
                    cout<<'k';

                else if(a[i]=='p')
                    cout<<'r';

                else if(a[i]=='q')
                    cout<<'z';

                else if(a[i]=='r')
                    cout<<'t';

                else if(a[i]=='s')
                    cout<<'n';

                else if(a[i]=='t')
                    cout<<'w';

                else if(a[i]=='u')
                    cout<<'j';

                else if(a[i]=='v')
                    cout<<'p';

                else if(a[i]=='w')
                    cout<<'f';

                else if(a[i]=='x')
                    cout<<'m';

                else if(a[i]=='y')
                    cout<<'a';

                else if(a[i]=='z')
                    cout<<'q';


            }
            else
                cout<<a[i];

        }
        cout<<endl;




    }

}

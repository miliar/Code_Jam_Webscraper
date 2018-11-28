#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
 
using namespace std;
 
int main()
{
        int n;
        scanf("%i", &n);
        for(int i=1;i<=n;i++)
        {
                int t, s, p;
                int total=0;
                cin>>t>>s>>p;
                for(int j=0;j<t;j++)
                {
                        double atual;
                        cin>>atual;
                        if(ceil(atual/3)>=p)
                                total++;
                        else if(ceil(atual/3)+1>=p && s>0 && atual>1)
                        {
                                total++;
                                s--;
                        }
                }
                cout<<"Case #"<<i<<": "<<total<<endl;
        }
}
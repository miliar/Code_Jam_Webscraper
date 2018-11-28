#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
using namespace std;

int main()
{
    int test;
    cin>>test;
    int mycase=0;
int store=0;
int a,b,c;
    while(test--)
    {
        mycase++;
        int i;
        cin>>a>>b>>c;
        store=0;

        for(i=1;i<=a;i++)
        {
            int inp;
            cin>>inp;

            if(inp>3*c-1)
                    {
                        store++;
                        continue;
                        //store--;
                    }
                    else
                    {
                        if(c>=1)
                        //if(c-1>=0
                        {
                            if(inp==(3*c-1))
                            {
                                store++;
                                continue;
                            }
                    else if(inp==(3*c-2))
                    {
                        store++;
                        continue;
                    }
                            else if(c>=2)
                            {
                                if(inp==(3*c-3) && b)
                                {
                                    store++;
                                    b--;
                                    continue;
                                }
                                else if(inp==(3*c-4) && b)
                                {
                                    store++;
                                    b--;
                                    continue;
                                }

                            }
                }
            }
        }
        cout<<"Case #"<<mycase<<": "<<store<<"\n";

    }
}

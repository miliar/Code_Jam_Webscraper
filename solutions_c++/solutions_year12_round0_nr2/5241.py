/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 11:44:25 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Amir Hardon (), ahardon@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <iostream>
#include <assert.h>

using namespace std;
int main(void)
{

        int t,n,s,p;
        cin>>t;
        for(int x=1; x<=t; x++)
        {
                cin>>n;
                cin>>s;
                cin>>p;
                int count=0;
                for(int i=0; i<n; i++)
                {
                        int sum;
                        cin>>sum;
                        int a = sum/3;
                        //cout<<"sum="<<sum<<endl;
                        //cout<<"sum%3="<<sum%3<<endl;
                        //cout<<"a="<<a<<endl;
                        switch (sum % 3)
                        {
                                case 0: // a a a or a a+1 a+2
                                        if(a>=p) // a a a
                                        {
                                                count++;
                                                continue;
                                        }
                                        if(s>0 && a+1 >=p  && a-1 >=0 ) // a-1 a a+1
                                        {
                                                count++;
                                                s--;
                                                continue;
                                        }
                                        break;
                                case 1: // a a+1 a+1 or a a a+2
                                        if(a+1 >= p)
                                        {
                                                count++;
                                                continue;
                                        }
                                        if(s>0 && a+2 >=p)
                                        {

                                                s--;
                                                count++;
                                        }
                                        break;
                                case 2: // x x+1 x+1 or x x x+2
                                        if(a+1 >= p)
                                        {
                                                count++;
                                                continue;
                                        }
                                        if(s>0 && a+2 >= p)
                                        {
                                                s--;
                                                count++;
                                        }
                                        break;

                        }

                }
                cout<<"Case #"<<x<<": "<<count<<endl;
        }


}


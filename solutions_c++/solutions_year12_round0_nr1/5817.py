/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 09:18:19 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Amir Hardon (), ahardon@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

const char *plain =  "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
const char *cipher = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";

#define LET_NUM ('z'-'a' +1)
char translation[LET_NUM];

using namespace std;

int main(void)
{
        int x, len;
        char ch;
        len = strlen(plain);
        memset(translation,0,LET_NUM);
        for(x=0; x<len; x++)
        {
                ch=cipher[x];
                if(ch >= 'a' && ch<='z')
                {
                        if(translation[ch - 'a']!=0)
                        {
                                assert(translation[ch - 'a']==plain[x]);
                        }
                        translation[ch-'a']=plain[x];
                }
        }

        //for(x=0; x<LET_NUM; x++)
        //{
                //cout<<(char)('a'+(char)x)<<" => ";
                //if(translation[x]!=0)
                        //cout<<translation[x];
                //cout<<endl;
        //}

        int n;
        size_t bufSize=102;
        char buf[102];
        cin>>n;
        cin.getline(buf,bufSize);
        for(x=1; x<=n; x++)
        {
                cin.getline(buf,bufSize);
                cout<<"Case #"<<x<<": ";
                for(int i=0; buf[i]!='\0'; i++)
                {
                        if(buf[i] >='a' && buf[i]<='z')
                        {
                                cout<<translation[buf[i]-'a'];
                        }
                        else
                        {
                                cout<<buf[i];
                        }
                }
                cout<<endl;
        }

        return 0;

}

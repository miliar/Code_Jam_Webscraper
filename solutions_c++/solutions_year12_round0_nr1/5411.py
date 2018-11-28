#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
using namespace std;

void arrange(int l, string str, char a[]);

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,t;
    int count = 0;
    //char str[100] = {0};
    string str;
    char a[100] = {0};
    cin>>t;
getline(cin,str);
    while(t--)
    {
        getline(cin,str);
        int l = str.size();
        //cout<<"l is "<<l;
        //cout<<str<<endl;
        arrange(l,str,a);
        count++;
        cout<<"Case #"<<count<<": ";
        for(i=0;i<l;i++)
            cout<<a[i];
        cout<<endl;
    }
    return 0;
}

void arrange(int l, string str, char a[])
{
    int i;
    for(i=0;i<l;i++)
    {
        if(str[i]==' ')
        a[i] = ' ';
        else
        {

            switch (str[i])
            {
                case 'y':
                    a[i] = 'a';
                    break;
                case 'n':
                    a[i] = 'b';
                    break;
                case 'f':
                    a[i] = 'c';
                    break;
                case 'i':
                    a[i] = 'd';
                    break;
                case 'c':
                    a[i] = 'e';
                    break;
                case 'w':
                    a[i] = 'f';
                    break;
                case 'l':
                    a[i] = 'g';
                    break;
                case 'b':
                    a[i] = 'h';
                    break;
                case 'k':
                    a[i] = 'i';
                    break;
                case 'u':
                    a[i] = 'j';
                    break;
                case 'o':
                    a[i] = 'k';
                    break;
                case 'm':
                    a[i] = 'l';
                    break;
                case 'x':
                    a[i] = 'm';
                    break;
                case 's':
                    a[i] = 'n';
                    break;
                case 'e':
                    a[i] = 'o';
                    break;
                case 'v':
                    a[i] = 'p';
                    break;
                case 'z':
                    a[i] = 'q';
                    break;
                case 'p':
                    a[i] = 'r';
                    break;
                case 'd':
                    a[i] = 's';
                    break;
                case 'r':
                    a[i] = 't';
                    break;
                case 'j':
                    a[i] = 'u';
                    break;
                case 'g':
                    a[i] = 'v';
                    break;
                case 't':
                    a[i] = 'w';
                    break;
                case 'h':
                    a[i] = 'x';
                    break;
                case 'a':
                    a[i] = 'y';
                    break;
                case 'q':
                    a[i] = 'z';
                    break;

            }
        }
    }
}

#include <iostream>
#include <fstream>
#include <string.h>
#define MAX 110

using namespace std;

int main()
{
    fstream in,out;
    in.open("dat.in",ios::in);
    out.open("out.dat",ios::out);

    char map[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    int asc = 97;

    int n;
    in>>n;cout<<"lines : "<<n<<"\n";
    char nop[MAX];
    in.getline(nop,MAX);

    for(int i=0;i<n;i++)
    {
        char line[MAX];
        memset(&line,'\0',MAX);
        in.getline(line,MAX);

        cout<<line<<"\n";
        int len = strlen(line);

        for(int j = 0;j<len;j++)
        {
            if(line[j] == ' ')
            continue;

            int a = line[j];
            int index = a - asc;
            int replace;

            for(int k =0; k<strlen(map);k++)
            {
                if(line[j]==map[k])
                {
                    replace = 97 + k;
                    break;
                }
            }

            line[j] = replace;

        }

        cout<<line<<"\n\n";
        out<<"Case #"<<i+1<<": "<<line<<"\n";

    }
}

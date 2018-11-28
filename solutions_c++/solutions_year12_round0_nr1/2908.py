#include<iostream>
#include<map>
#include<cstdio>
#include<string>
using namespace std;

char g[105];
int t;
int converts[28];
int vis[28];

int main()
{
    memset(converts,0,sizeof(converts));
    memset(g , 0 ,sizeof(g));
	memset(vis , 0 , sizeof(vis) ) ;
    converts['y' - 97] = 'a';
    converts['e' - 97] = 'o';
    converts['q' - 97] = 'z';
	vis['z' - 97] = 1;
    map<string,string> maps; //×Öµä
    maps.insert(make_pair("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"));
    maps.insert(make_pair("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"));
    maps.insert(make_pair("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up"));
    map<string,string>::iterator it = maps.begin();
    for( ; it != maps.end() ; ++it)
    {
        string k = it->first;
        string v = it->second;
        for(int i = 0 ; i < k.length() ; ++i)
        {
            if(k[i] != ' ')
            {
				
                converts[k[i]-97] = v[i];
				vis[v[i]-97] = 1;
            }
        }

    }
	for(int i = 0 ; i < 26 ; ++i)
	{
		if( !converts[i] )
		{
			for(int j = 'a' ; j <= 'z' ; ++j)
			{
				if(!vis[j-97])
					converts[i] = j;
			}
			break;
		}
	}

		//freopen("in.in" , "r" , stdin);
    //freopen("out.txt" , "w" ,stdout);
    cin >> t;

    getchar();
    for(int i = 1; i<=t ;++i)
    {
        memset(g, 0,sizeof(g));
        cin.getline(g,105);

 

        for(int j = 0 ; j < strlen(g) ; ++j)
        {
            if(g[j] != ' ')
            {
                                g[j] = converts[g[j]-97];
            }

        }
        cout << "Case #" << i  << ": "<<g << endl;


    }
    return 0;
}

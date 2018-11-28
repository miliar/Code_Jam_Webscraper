#include <iostream>
#include <algorithm>
#define sz(x) (int)x.size()
using namespace std;

main()
{
 string buf;
 int T;
 scanf("%d ",&T);
 
 for(int q=0; q < T; q++)
 {
   	cin >> buf;
 	int i=sz(buf)-1;
 	bool swf=false;
 	for(; i >= 0; i--)
 	{
 		int min=100,minj=-1;
 		for(int j=i+1; j < sz(buf); j++)
 		{
 			if(buf[j] > buf[i] && buf[j] < (char)min)
 			{
 			min=buf[j];
 			minj=j;	
 			}
 		}
 		if(minj != -1 && buf[minj] > buf[i])
 		{
 		swf=true;
 		swap(buf[minj],buf[i]);
 		sort(buf.begin()+i+1,buf.end());
 		cout <<"Case #"<<q+1<<": "<< buf << endl;
 		break;
 	    }
 	}
 	if(!swf)
 	{
 	reverse(buf.begin(),buf.end());
 	if(buf[0] != '0')
 	{
 	buf=buf.substr(0,1)+"0"+buf.substr(1);
 	cout <<"Case #"<<q+1<<": "<< buf << endl;
 	}
 	else
 	{
 	 int c=0;
 	 string bufd;
 	 for(int i=0; i < sz(buf); i++)
 	 if(buf[i] == '0')
 	 c++;
 	 else
 	 bufd+=buf[i];
 	 
 	 sort(bufd.begin(),bufd.end());
 	 for(int i=0; i < c+1; i++)
 	 bufd=bufd.substr(0,1) + "0" + bufd.substr(1);
 	 cout <<"Case #"<<q+1<<": "<< bufd << endl;
 	}
 	
 	}
 }
}

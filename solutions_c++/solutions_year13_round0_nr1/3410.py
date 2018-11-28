    #include <vector>
    #include <list>
    #include <map>
    #include <queue>
    #include <set>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #include <stdio.h>
    #include <stdlib.h>
    using namespace std;
     
    int main(){
       freopen ("myfile.txt","w",stdout);freopen ("A-large.in","r",stdin);
        int i,j,k;
		int n;
		char c,t='T';
		bool b;
		cin>>n;
		string a[4];

		for(int q=1;q<=n;q++){
			b=false;
			for(i=0;i<4;i++)
				cin>>a[i];
				
			c='X';

			for(i=0;i<4;i++)
				if((a[i][0]==c || a[i][0]==t) && (a[i][1]==c || a[i][1]==t) && (a[i][2]==c || a[i][2]==t) && (a[i][3]==c || a[i][3]==t)){
					b=true;
					cout<<"Case #"<<q<<": X won"<<endl;
				}
				if(b)
					continue;
			c='O';

			for(i=0;i<4;i++)
				if((a[i][0]==c || a[i][0]==t) && (a[i][1]==c || a[i][1]==t) && (a[i][2]==c || a[i][2]==t) && (a[i][3]==c || a[i][3]==t)){
					b=true;
					cout<<"Case #"<<q<<": O won"<<endl;
				}
				if(b)
					continue;
			
			c='X';

			for(i=0;i<4;i++)
				if((a[0][i]==c || a[0][i]==t) && (a[1][i]==c || a[1][i]==t) && (a[2][i]==c || a[2][i]==t) && (a[3][i]==c || a[3][i]==t)){
					b=true;
					cout<<"Case #"<<q<<": X won"<<endl;
				}
				if(b)
					continue;
				
			c='O';

			for(i=0;i<4;i++)
				if((a[0][i]==c || a[0][i]==t) && (a[1][i]==c || a[1][i]==t) && (a[2][i]==c || a[2][i]==t) && (a[3][i]==c || a[3][i]==t)){
					b=true;
					cout<<"Case #"<<q<<": O won"<<endl;
				}
				if(b)
					continue;
			
			c='X';
			if(((a[0][0]==c || a[0][0]==t) && (a[1][1]==c || a[1][1]==t) && (a[2][2]==c || a[2][2]==t) && (a[3][3]==c || a[3][3]==t)) || ( (a[0][3]==c || a[0][3]==t) && (a[1][2]==c || a[1][2]==t) && (a[2][1]==c || a[2][1]==t) && (a[3][0]==c || a[3][0]==t)))
			{
				cout<<"Case #"<<q<<": X won"<<endl;
				continue;
			}

			c='O';
			if(((a[0][0]==c || a[0][0]==t) && (a[1][1]==c || a[1][1]==t) && (a[2][2]==c || a[2][2]==t) && (a[3][3]==c || a[3][3]==t)) || ( (a[0][3]==c || a[0][3]==t) && (a[1][2]==c || a[1][2]==t) && (a[2][1]==c || a[2][1]==t) && (a[3][0]==c || a[3][0]==t)))
			{
				cout<<"Case #"<<q<<": O won"<<endl;
				continue;
			}
			
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					if(a[i][j]=='.')
						b=true;

			if(b)
				cout<<"Case #"<<q<<": Game has not completed"<<endl;
			else
				cout<<"Case #"<<q<<": Draw"<<endl;

		}

        



       //    system("PAUSE");
           return 0;
           }

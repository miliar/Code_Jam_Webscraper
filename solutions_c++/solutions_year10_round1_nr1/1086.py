#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <ctime>
#include <sstream>

using namespace std;

void displayvec(vector<int> vec)
{
	for(int i=0;i<vec.size();i++){
		cout << vec[i] << " ";
	}
	cout << endl;

	return ;
}

int main(void)
{
    freopen("data1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    
    for(int k=1;k<=t;k++){
		int n;
		int x;
		scanf("%d",&n);
		scanf("%d",&x);

		vector<vector<char> > ini(n,vector<char>(n,'.'));
		vector<vector<char> > vec=ini;
		vector<vector<char> > ans=ini;

		int max_col=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				char temp;
				scanf("%c",&temp);
				if(temp!='R' && temp!='.' && temp!='B'){
					j--;
					continue;
				}
			//	cout << temp << " ";
				ini[i][j]=temp;
				if(temp!='.'){
					if(j>max_col){
						max_col=j;
					}
				}
			}
		}
		
		int count=0,flag=0;
		for(int i=0;i<n;i++){
			count=0;
			flag=0;
			for(int j=vec.size()-1;j>-1;j--){
				if(j<=max_col){
					if(ini[i][j]=='.' && flag==0){
						count++;
					}else{
						flag=1;
						vec[j+count][n-1-i]=ini[i][j];
					}
				}
			}
		}

		
		for(int i=0;i<=max_col;i++){
			for(int j=0;j<vec[i].size();j++){
				ans[i+(n-1-max_col)][j]=vec[i][j];
			}
		}
		
		for(int i=0;i<n;i++){
			for(int j=n-1;j>-1;j--){
				if(ans[j][i]=='.'){
					for(int p=j;p>-1;p--){
						if(ans[p][i]!='.'){
							swap(ans[j][i],ans[p][i]);
							break;
						}
					}
				}
			}
		}
				
		int counta=0;
		int countb=0;
		bool testa=false;
		bool testb=false;
		
		for(int i=0;i<ans.size();i++){
			counta=0;
			countb=0;
			for(int j=0;j<ans[i].size();j++){
				if(ans[i][j]=='R'){
					counta++;
					countb=0;
					if(counta==x)testa=true;
				}else if(ans[i][j]=='B'){
					counta=0;
					countb++;
					if(countb==x)testb=true;
				}else{
					counta=0;
					countb=0;
				}
			}
		}
		for(int i=0;i<ans.size();i++){
			counta=0;
			countb=0;
			for(int j=0;j<ans[i].size();j++){
				if(ans[j][i]=='R'){
					counta++;
					countb=0;
					if(counta==x)testa=true;
				}else if(ans[j][i]=='B'){
					counta=0;
					countb++;
					if(countb==x)testb=true;
				}else{
					counta=0;
					countb=0;
				}
			}
		}

  		vector<vector<int> > a(n,vector<int>(n,1));
        for(int i=0;i<ans.size();i++){
			for(int j=0;j<ans[i].size();j++){
				if(i-1>-1 && i-1<n && j-1>-1 && j-1<n && ans[i-1][j-1]==ans[i][j] && ans[i][j]!='.'){
					a[i][j]=a[i-1][j-1]+1;
				}
			}
		}
		vector<vector<int> > ab(n,vector<int>(n,1));
        for(int i=0;i<ans.size();i++){
			for(int j=0;j<ans[i].size();j++){
				if(i-1>-1 && i-1<n && j+1>-1 && j+1<n  && ans[i-1][j+1]==ans[i][j] && ans[i][j]!='.'){
					ab[i][j]=ab[i-1][j+1]+1;
				}
			}
		}

		for(int i=0;i<a.size();i++){
			for(int j=0;j<a[i].size();j++){
				if(a[i][j]==x){
					if(ans[i][j]=='R'){
						testa=true;
					}else{
						testb=true;
					}
				}
				if(ab[i][j]==x){
					if(ans[i][j]=='R'){
						testa=true;
					}else{
						testb=true;
					}
				}
			}
		}
		
		if(testa && testb){
			cout << "Case #" << k << ": Both" <<endl;
		}else if(!testa && !testb){
            cout << "Case #" << k << ": Neither" <<endl;
		}else if(testa && !testb){
            cout << "Case #" << k << ": Red" <<endl;
		}else if(!testa && testb){
            cout << "Case #" << k << ": Blue" <<endl;
		}
		/*for(int j=0;j<n;j++){
			for(int i=0;i<a.size();i++){
				cout << vec[j][i] << " ";
			}
			cout << endl;
		}*/
        
		
	}

    fclose(stdin);
	fclose(stdout);
	//system("pause");
	return 0;
}


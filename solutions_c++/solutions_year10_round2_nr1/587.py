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

void displayvec(vector<string> vec)
{
	for(int i=0;i<vec.size();i++){
		cout << vec[i] << " ";
	}
	cout << endl;

	return ;
}

vector<string> parse(string s){
    string temp="";
    vector<string> vec;
    for(int i=0;i<s.size();i++){
        if(i+1<s.size() && s[i+1]=='/'){
            temp.push_back(s[i]);
			vec.push_back(temp);
        }else{
            temp.push_back(s[i]);
        }
    }
    vec.push_back(temp);

    return vec;
}
int main(void)
{
    freopen("data1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int k=1;k<=t;k++){
        int n,m;
        scanf("%d",&n);
        scanf("%d",&m);


        map<string,bool> mp;
        for(int i=0;i<n;i++){
            string s;
            cin >> s;

            vector<string> vec;

            vec=parse(s);


            for(int j=0;j<vec.size();j++){
                if(mp.count(vec[j])==0){
                    mp[vec[j]]=true;
                }
            }
            //displayvec(vec);

        }

        int count=0;
        for(int i=0;i<m;i++){
            string s;
            cin >> s;

            vector<string> vec;
            vec=parse(s);


            for(int j=0;j<vec.size();j++){
                if(mp.count(vec[j])==0){
                    count++;
                    mp[vec[j]]=true;
                }
            }
        }

        printf("Case #%d: %d\n",k,count);


    }

    fclose(stdin);
    fclose(stdout);
    //system("pause");
    return 0;



}

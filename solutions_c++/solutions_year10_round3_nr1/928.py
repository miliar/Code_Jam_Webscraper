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
        scanf("%d",&n);

        vector<vector<int> >vec(n,vector<int>(2,-1));
        vector<int> vec2;

        for(int i=0;i<n;i++){
            int temp;
            scanf("%d",&temp);
            vec[i][0]=temp;
            scanf("%d",&temp);
            vec[i][1]=temp;
            vec2.push_back(temp);
        }

        sort(vec2.begin(),vec2.end());
        sort(vec.begin(),vec.end());

        int count=0;
        for(int i=0;i<vec.size();i++){
            for(int j=i+1;j<vec.size();j++){
                if(vec[j][1]<vec[i][1]){
                    count++;
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

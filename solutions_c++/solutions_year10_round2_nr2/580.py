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

void displayvec(vector<long long> vec)
{
	for(int i=0;i<vec.size();i++){
		cout << vec[i] << " ";
	}
	cout << endl;

	return ;
}


int main(void)
{
    freopen("data2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int c;
    scanf("%d",&c);

    for(int p=1;p<=c;p++){
        long long n,k,b;
        int t;
        scanf("%lld",&n);
        scanf("%lld",&k);
        scanf("%lld",&b);
        scanf("%d",&t);

        vector<long long> dist;
        for(int i=0;i<n;i++){
            long long temp;
            cin >> temp;
            dist.push_back(temp);
        }
        vector<double> speed;
        for(int i=0;i<n;i++){
            double temp;
            cin >> temp;
            speed.push_back(temp);
        }

        sort(dist.rbegin(),dist.rend());
		reverse(speed.begin(),speed.end());
		//displayvec(dist);

        int count=0;
        int loser=0;
        for(int i=0;i<dist.size();i++){
            double sped= (double)(b-dist[i])/(double)t;
            if(speed[i]>=sped){
                k--;
                count+=loser;
                if(k==0)break;
            }else{
                loser++;
            }
        }
		if(k!=0){
            printf("Case #%d: IMPOSSIBLE\n",p);
		}else{
	        printf("Case #%d: %d\n",p,count);
		}

    }

    fclose(stdin);
    fclose(stdout);
    //system("pause");
    return 0;

}

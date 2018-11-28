#include <cstdio>
#include <map>
#include <vector>

using namespace std;


map<vector<unsigned long>, unsigned long long>mapp;
map<vector<unsigned long>, unsigned long long>::iterator mit;

vector<unsigned long long> total;

unsigned long long value_vec(vector <unsigned long> &vec, unsigned long k)
{
	//for(int ii=0; ii<vec.size(); ii++)printf("%ld ",  vec[ii]);
	//printf("\n");

	vector<unsigned long> tv;
	unsigned long long ans=0;
	
	unsigned ct=0;
	while(ct<vec.size() && k>=vec[ct]+ans)
	{
		ans+= vec[ct];
		tv.push_back(vec[ct]);
		ct++;
	}
	if(ct==vec.size()) return ans;
	
	vec.erase(vec.begin(), vec.begin()+ct);
	for(ct=0; ct<tv.size(); ct++)
		vec.push_back(tv[ct]);
	
	//printf("%lld\n", ans);
	return ans;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	unsigned long t, r, k, n;
	scanf("%ld", &t);
	for(unsigned icase=0; icase<t; icase++)
	{
		scanf("%ld%ld%ld", &r, &k, &n);
		unsigned long g;
		vector<unsigned long> vec;
		vec.clear();
		for(unsigned long j=0; j<n; j++)
		{
			scanf("%ul", &g);
			vec.push_back(g);
		}
		vector<unsigned long> tvec;
		
		total.clear();
		mapp.clear();
		total.push_back(0);

		tvec=vec;

		unsigned long long counter=1;
		total.push_back(value_vec(vec, k));
		
		mapp[tvec]=counter++;
		
		mit=mapp.find(vec);
		while(mit==mapp.end() && counter<=r)
		{
			tvec=vec;
			total.push_back(total[counter-1] + value_vec(vec, k));
			mapp[tvec] = counter++;
			mit=mapp.find(vec);
		}
		
		unsigned long long ans = 0;
		
		if(counter>r)
		{
			ans = total[counter-1];
		}
		else
		{
			unsigned long long start = (*mit).second;
			unsigned long long dd = total[counter-1] - total[start-1];
			unsigned long long tres=(r - start)%(counter-start);
			ans = ((r - start)/(counter-start))*dd + total[start+tres]; 
		}
		printf("Case #%d: %lld\n", icase+1, ans);
	}
	return 0;
}
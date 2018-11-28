#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;


main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		printf("Case #%d: ",casenum);
		double x,s,r,t;
		int n;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		double l[1010];
		double v[1010];
		double nokori=x;
		double ans=0;
		for(int i=0;i<n;i++){
			double b,e;
			scanf("%lf%lf%lf",&b,&e,&v[i]);
			l[i]=e-b;
			nokori-=l[i];
			ans+=l[i]/(v[i]+s);
		}
		if(nokori>1e-9){
			v[n]=0;
			l[n]=nokori;
			ans+=nokori/s;
			n++;
		}
		vector<pair<double, double> > hoge;
		for(int i=0;i<n;i++){
			double mt=l[i]/(v[i]+r);
			double yotei=l[i]/(v[i]+s);
			double toku=(yotei-mt)/mt;
			hoge.push_back(make_pair(toku,mt));
		}
		sort(hoge.begin(),hoge.end());
		reverse(hoge.begin(),hoge.end());
		double hasitta=0;
		for(int i=0;i<n;i++){
			if(hasitta+hoge[i].second>=t){
				ans-=hoge[i].first*(t-hasitta);
				break;
			}
			hasitta+=hoge[i].second;
			ans-=hoge[i].first*hoge[i].second;
		}
		printf("%.12f\n",ans);
	}
}
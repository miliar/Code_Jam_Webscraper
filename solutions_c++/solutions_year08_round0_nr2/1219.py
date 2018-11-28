#include<iostream>
#include<queue>
#include<vector>
using namespace std;

struct point{
	int time;
	bool wh; // 0 A , 1 B
	bool flag; // 0 leave, 1 arrive
	point(int t, bool w, bool f){ time = t; wh = w; flag = f; }
};

bool cmp(point s, point t)
{
	if(s.time<t.time || (s.time==t.time&&s.flag==1)) return true;
	return false;
}

vector<point> v;

int main()
{
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\B-large.in","r",stdin);
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\B.out","w",stdout);
	int i,j,k,r,t,tr,na,nb;
	scanf("%d",&t);
	int s1,s2,s3,s4;
	char c, s[100];
	for(i=0; i<t; i++)
	{
		v.clear();
		scanf("%d",&tr);
		scanf("%d%d",&na,&nb);
		//getchar();
		for(j=0; j<na; j++)
		{
			scanf("%d:%d",&s1,&s2);
			s2 += s1*60;
			v.push_back(point(s2,0,0));

			scanf("%d:%d",&s1,&s2);
			s2 += s1*60;
			s2 +=tr;
			v.push_back(point(s2,0,1));
			/*c = getchar();
			s1 = (c-'0')*10;
			c = getchar();
			s1 += c-'0';

			getchar();

			c = getchar();
			s2 = (c-'0')*10;
			c = getchar();
			s2 += c-'0';

			getchar();
			s2 += 60 * s1;
			v.push_back(point(s2,0,0));

			c = getchar();
			s3 = (c-'0')*10;
			c = getchar();
			s3 += c-'0';

			getchar();

			c = getchar();
			s4 = (c-'0')*10;
			c = getchar();
			s4 += c-'0';

			getchar();
			s4 += 60 * s3;
			s4 += tr;
			v.push_back(point(s4,0,1));*/
		}
		for(j=0; j<nb; j++)
		{
			scanf("%d:%d",&s1,&s2);
			s2 += s1*60;
			v.push_back(point(s2,1,0));

			scanf("%d:%d",&s1,&s2);
			s2 += s1*60;
			s2 +=tr;
			v.push_back(point(s2,1,1));

			/*c = getchar();
			s1 = (c-'0')*10;
			c = getchar();
			s1 += c-'0';

			getchar();

			c = getchar();
			s2 = (c-'0')*10;
			c = getchar();
			s2 += c-'0';

			getchar();
			s2 += 60 * s1;
			v.push_back(point(s2,1,0));

			c = getchar();
			s3 = (c-'0')*10;
			c = getchar();
			s3 += c-'0';

			getchar();

			c = getchar();
			s4 = (c-'0')*10;
			c = getchar();
			s4 += c-'0';

			getchar();
			s4 += 60 * s3;
			s4 += tr;
			v.push_back(point(s4,1,1));*/
		}
		sort(v.begin(),v.end(),cmp);
		//for(j=0; j<v.size(); j++) printf("%d ",v[j].time);
		//printf("\n");
		int ah = 0, bh = 0, a = 0 , b = 0;
		for(j=0; j<v.size(); j++)
		{
			//cout<<ah<<" "<<bh<<" "<<a<<" "<<b<<endl;
			//cout<<v[j].time<<" "<<v[j].wh<<" "<<v[j].flag<<endl;
			if(v[j].flag==1)
			{
				if(v[j].wh==1) ah++;
				else bh++;
				continue;
			}
			if(v[j].wh==0) // leave A
			{
				if(ah>0) ah--;
				else a++;
				continue;
			}
			if(v[j].wh==1) // leave B
			{
				if(bh>0) bh--;
				else b++;
				continue;
			}
		}
		printf("Case #%d: %d %d\n",i+1,a,b);
	}
	return 0;
}


#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito = 1;casito<=casos;casito++)
	{
	    vector<pair<int,int> > vec;
	    int n;
	    cin >> n;
	    char c;
	    int k;
	    //vec.push_back(make_pair(0,1));
	    //vec.push_back(make_pair(1,1));
	    forn(i,n)
	    {
	        cin >> c >> k;
	        if(c=='O')
                vec.push_back(make_pair(0,k));
            else
                vec.push_back(make_pair(1,k));
	    }
	    int pos0 = 1, pos1 = 1, time = -1;
	    int punt0 = 0, punt1 = 0;
	    while(punt0<vec.size()&&vec[punt0].first==1)
            punt0++;
        while(punt1<vec.size()&&vec[punt1].first==0)
            punt1++;
        bool b0 = false, b1 = false, bbb = false, bbb2 = false;
	    while(punt0!=vec.size()||punt1!=vec.size()||bbb==true || bbb2==true)
	    {
            bbb = false;
            bbb2 = false;
            if(punt0!=vec.size()&&pos0==vec[punt0].second&&punt0<punt1)
            {
                bbb = true;
                punt0++;
                while(punt0<vec.size()&&vec[punt0].first==1)
                    punt0++;
            }
            else if(punt0!=vec.size())
            {
                if(pos0<vec[punt0].second)
                    pos0++;
                else if(pos0>vec[punt0].second)
                    pos0--;
            }
	        if(punt1!=vec.size()&&pos1==vec[punt1].second&&bbb==false&&punt1<punt0)
	        {
	            bbb2 = true;
                punt1++;
                while(punt1<vec.size()&&vec[punt1].first==0)
                    punt1++;
	        }
	        else if(punt1 != vec.size())
	        {
                if(pos1<vec[punt1].second)
                    pos1++;
                else if(pos1>vec[punt1].second)
                    pos1--;
	        }
	        time++;
	    }
	    cout << "Case #"<< casito << ": "<< time << endl;
	}
}

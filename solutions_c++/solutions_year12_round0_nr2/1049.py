#include<fstream>
#include<sstream>
#include<vector>
#include<string>
#include<string.h>

using namespace std;

//vector<int> nums1;   //ƽ���������ڵ���P��
//vector<int> nums2;   //ƽ������С��P��

int main()
{  
    ifstream fin("B-large.in");//B-small-attempt2.
	ofstream fout("B-large.txt");
	int T;
	fin>>T;
	string line;
	for(int i=0; i!=T; ++i)
	{   int N,S,P;
	    fin>>N>>S>>P;
		int ans=0;
		vector<int> nums1,nums2;
		for(int j=0;j!=N; ++j)
		{   int tmpPt;
		    fin>>tmpPt;
			if(tmpPt/3>=P || (tmpPt%3>0 && (tmpPt/3)+1>=P))
			    nums1.push_back(tmpPt);
			else
                nums2.push_back(tmpPt);
		}
		ans = nums1.size();
        int tmpS = 0;
		int k=0;
        while(tmpS<S && k!=nums2.size())
        {   if((nums2.at(k)%3==2 && nums2.at(k)/3+2>=P && nums2.at(k)/3<=8) || (nums2.at(k)%3==0 && nums2.at(k)/3+1>=P && nums2.at(k)/3<=9 && nums2.at(k)/3>0))
			{   ++ans;
				++tmpS;
			}
			++k;
		}
	    fout<<"Case #"<<i+1<<": ";
		fout<<ans<<endl;
	}
	return 0;
}
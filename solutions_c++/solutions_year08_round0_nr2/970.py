#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <functional>

using namespace std;
struct Time
{
	Time(int h, int m):m_iH(h),m_iM(m){}
	Time(string str)
	{
		int iPos = str.find(':');
		string str2;
		str2.assign(str.begin(), str.begin() + iPos);
		m_iH = atoi(str2.c_str());
		iPos++;
		str2.assign(str.begin() + iPos, str.end());
		m_iM = atoi(str2.c_str());

	}
	bool operator== (const Time& tm)
	{
		return tm.m_iM == m_iM && tm.m_iH == m_iH;
	}
	bool operator< (const Time& tm) 
	{
		if( m_iH < tm.m_iH )
			return true;
		else if( m_iH == tm.m_iH)
		{
			if( m_iM < tm.m_iM )
				return true;
			else
				return false;
		}
		else
			return false;
	}
	Time& operator+=(int min)
	{
		m_iM += min;
		if( m_iM >= 60 )
		{
			m_iH++;
			m_iM -= 60;
		}
		return *this;
	}
	Time& operator+=(const Time& tm)
	{
		m_iM += tm.m_iM;
		if( m_iM >= 60 )
		{
			m_iH++;
			m_iM -= 60;
		}
		m_iH += tm.m_iH;
		return *this;
	}
	int m_iH;
	int m_iM;
};

struct Train
{
	Train(Time td, Time ta): m_tDepart(td), m_tArriv(ta){}
	Time m_tDepart;
	Time m_tArriv;
	bool operator< (const Train& tr) 
	{
		return m_tArriv < tr.m_tArriv;
	}
	bool operator== (const Train& tr) 
	{
		return m_tArriv == tr.m_tArriv && m_tDepart == tr.m_tDepart;
	}
};


int main( int argc, char*argv[])
{
    if( argc != 2 )
    {
        cout<<"Specify input file please.\n";
        return 1;
    }
    ifstream in(argv[1]);
    string sFile = argv[1];
    sFile.replace(sFile.length() - 2, 2, "out");
    ofstream out(sFile.c_str());
    string str;
    getline(in,str);
    int iTasks = atoi(str.c_str());
    for( int iCount = 1; iCount <= iTasks; iCount++ )
    {
		getline(in, str);
		int iTurn = atoi(str.c_str());
		getline(in, str);
		int iPos = str.find(' ');
        string str2;
        str2.assign(str.begin(), str.begin() + iPos);
		int iAtrains = atoi(str2.c_str());
		iPos++;
		str2.assign(str.begin() + iPos, str.end());
		int iBtrains = atoi(str2.c_str());
		vector<Train> vASched;
		vector<Train> vBSched;
		int iFromA = iAtrains, iFromB = iBtrains;
		for( int i = 0; i < iAtrains + iBtrains; i++ )
		{
			getline(in, str);
			iPos = str.find(' ');
			str2.assign(str.begin(), str.begin() + iPos);
			Time td(str2);
			iPos++;
			str2.assign(str.begin() + iPos, str.end());
			Time ta(str2);
			if( i >= iAtrains )
				vBSched.push_back(Train(td,ta));	
			else
				vASched.push_back(Train(td,ta));
		}
		vector<Train> vASched1(vASched);
		vector<Train> vBSched1(vBSched);
		vector<Train> vATmp;
		for( int i = 0; i < (int)vASched.size(); i++ )
		{
			vATmp.clear();
			for( int j = 0; j < (int)vBSched1.size(); j++ )
			{
				Time tmp = vBSched1[j].m_tArriv;
				tmp += iTurn; 
				if( !(vASched[i].m_tDepart < tmp) || vASched[i].m_tDepart == tmp )
				{
					vATmp.push_back(vBSched1[j]);
				}
			}
			if(!vATmp.empty())
			{
				sort(vATmp.begin(), vATmp.end());
				vector<Train>::iterator iter = find( vBSched1.begin(), vBSched1.end(), vATmp.back() ); 
				vBSched1.erase(iter);
				iFromA--;
			}
		}
		vATmp.clear();
		for( int i = 0; i < (int)vBSched.size(); i++ )
		{
			vATmp.clear();
			for( int j = 0; j < (int)vASched1.size(); j++ )
			{
				Time tmp = vASched1[j].m_tArriv;
				tmp += iTurn; 
				if( !(vBSched[i].m_tDepart < tmp) || vBSched[i].m_tDepart == tmp )
				{
					vATmp.push_back(vASched1[j]);
				}
			}
			if(!vATmp.empty())
			{
				sort(vATmp.begin(), vATmp.end());
				vector<Train>::iterator iter = find( vASched1.begin(), vASched1.end(), vATmp.back() ); 
				vASched1.erase(iter);
				iFromB--;
			}
		}
		out<<"Case #"<< iCount <<": "<<iFromA<<' '<<iFromB<<'\n';
	}
}
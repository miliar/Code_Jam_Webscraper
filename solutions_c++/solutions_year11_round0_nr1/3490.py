#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int case_cnt =0;
	int btn_cnt = 0;
	vector<int> btn;
	vector<char> rot;
	
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	if(!in)
	{
		cout<<"can not read the input file"<<endl;
		return 1;
	}
	in>>case_cnt;
	if(case_cnt <1 || case_cnt > 100) return 1;
	
	string temp;
	size_t opos=0;
	size_t bpos=0;
	size_t obeg=1;
	size_t bbeg=1;
	size_t count=0;
	size_t ostp=0;
	size_t bstp=0;
	size_t otstep;
	size_t btstep;
	int case_no = 1;
	char c;
	int no;
	while(case_cnt --)
	{
		btn.clear();
		rot.clear();
		count = 0;
		obeg = 1;
		ostp = 0;
		bbeg = 1;
		bstp = 0;
		otstep = 0;
		btstep = 0;
		in >> btn_cnt;
		if(btn_cnt<1 || btn_cnt > 100) return 1;
		for(int i=1;i<=2*btn_cnt;i++)
		{	
			if(i%2 == 0)
			{
				in>>no;		
				btn.push_back(no);
			}
			else
			{
				in>>c;			
				rot.push_back(c);
			}
		}
		for(size_t i=0;i< btn.size();i++)
		{
			if(rot[i] == 'O')
			{
				ostp = 1+ ((abs(btn.at(i) - obeg) <= btstep)?0:abs(btn.at(i) - obeg) - btstep);
				count += ostp;
				obeg = btn.at(i);
				otstep += ostp;
				btstep = 0;
			}
			else
				if(rot[i] =='B')
				{
					bstp = 1+ ((abs(btn.at(i) - bbeg) <= otstep)?0:abs(btn.at(i) - bbeg) - otstep);
					count += bstp;
					bbeg = btn.at(i);
					btstep += bstp;
					otstep = 0;
				}
				

		}
		out<<"Case "<<"#"<<case_no<<": "<<count<<endl;
		case_no++;

	
	}

	return 0;
}
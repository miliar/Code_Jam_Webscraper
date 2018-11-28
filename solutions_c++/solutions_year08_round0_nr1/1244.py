#define INFINITE 999999;
#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

int main(int argc, char *argv[])
{
	for(int i=0;i<argc;i++)
	{
		cout<<argv[i]<<endl;
	}
	if (argc<2)
	{
		exit(1);
	}
	string ifname(argv[1]);
	//string ifname("file.txt");
	ifstream ifile(ifname.c_str());
	ofstream ofile("outfile3.txt",ios::trunc);
	if(!ifile)
	{
		cerr<<"can not open"<<ifname;
	}
	if(!ofile)
	{
		cerr<<"can not open"<<ofile;
	}
	int casenum;
	ifile>>casenum;
	for(int j=0;j<casenum;j++)
	{
		vector<string> searchname;
		vector<string> set;
		int searchnum=0;
		int change=0;
		ifile>>searchnum;
		string tempstr;
		getline(ifile,tempstr);// white space;
		for(int k=0;k<searchnum;k++)
		{
			string temp;
			getline(ifile,temp);
			searchname.push_back(temp);
		}
		int querynum=0;
		vector<string> queryname;
		vector<int> querylabel;
		ifile>>querynum;
		getline(ifile,tempstr);
		for(int k=0;k<querynum;k++)
		{
			string temp;
			getline(ifile,temp);
			queryname.push_back(temp);
			for(int is=0;is<searchnum;is++)
			{
				if(temp==searchname[is])
				{
					querylabel.push_back(is);
					break;
				}
			}
		}
		vector<vector<int>> minDis (searchnum,vector<int>(querynum));
	
		if(querynum<2)
		{
			change=0;
		}
		else
		{//initie
			for (int is=0;is<searchnum;is++)
			{
				if(is==querylabel[0])
				{
					minDis[is][0]=INFINITE;
				}
				else
				{
					minDis[is][0]=0;
				}
			}
			for (int iq=1;iq<querynum;iq++)
			{
				for(int is=0;is<searchnum;is++)
				{
					if(is==querylabel[iq])
					{
						minDis[is][iq]=INFINITE;
					}
					else
					{
						int minValue=INFINITE;
						for(int ks=0;ks<searchnum;ks++)
						{
							int costvalue=0;
							if(ks==is)
							{
								costvalue=0;
							}
							else
							{
								costvalue=1;
							}
							if((minDis[ks][iq-1]+costvalue)<minValue)
								minValue=minDis[ks][iq-1]+costvalue;
						}
						minDis[is][iq]=minValue;
					}
				}
			}
			int minValue=INFINITE;
			for (int ms=0;ms<searchnum;ms++)
			{
				if(minDis[ms][querynum-1]<minValue)
					minValue=minDis[ms][querynum-1];
			}
			change=minValue;
		}
		ofile<<"Case #"<<j+1<<": "<<change<<endl;
	}

	ofile.clear();
	ofile.close();
	ifile.clear();
	ifile.close();
	return 0;
}

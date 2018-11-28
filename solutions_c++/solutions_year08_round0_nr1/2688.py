//#include <iostream>
//#include <fstream>
//#include <string>
//#include <vector>
//
//using namespace std;
//
//int main(int argc, char *argv[])
//{
//	for(int i=0;i<argc;i++)
//	{
//		cout<<argv[i]<<endl;
//	}
//	if (argc<2)
//	{
//		exit(1);
//	}
//	string ifname(argv[1]);
//	//string ifname("A-small-attempt0.in");
//	ifstream ifile(ifname.c_str());
//	ofstream ofile("outfile.txt",ios::trunc);
//	if(!ifile)
//	{
//		cerr<<"can not open"<<ifname;
//	}
//	if(!ofile)
//	{
//		cerr<<"can not open"<<ofile;
//	}
//	int casenum;
//	ifile>>casenum;
//	for(int j=0;j<casenum;j++)
//	{
//		vector<string> searchname;
//		vector<string> set;
//		int searchnum=0;
//		int change=0;
//		ifile>>searchnum;
//		string tempstr;
//		getline(ifile,tempstr);// white space;
//		for(int k=0;k<searchnum;k++)
//		{
//			string temp;
//			getline(ifile,temp);
//			searchname.push_back(temp);
//		}
//		int querynum=0;
//		vector<string> queryname;
//		ifile>>querynum;
//		getline(ifile,tempstr);
//		for(int k=0;k<querynum;k++)
//		{
//			string temp;
//			getline(ifile,temp);
//			queryname.push_back(temp);
//			vector<string>::size_type nindex=0;
//			for(nindex=0;nindex<set.size();nindex++)
//			{
//				if(set[nindex]==temp)
//				{
//					break;
//				}
//			}
//			if(nindex==set.size())
//			{
//				if(set.size()<searchnum-1)
//				{
//					set.push_back(temp);
//				}
//				else
//				{
//					change++;
//					set.clear();
//					set.push_back(temp);
//				}
//			}
//		}
//////////for end to first
//		int change2=0;
//		vector<string> set2;
//		for (int k=querynum-1;k>=0;k--)
//		{
//			vector<string>::size_type nindex=0;
//			string temp=queryname[k];
//		   // string test=queryname[0];
//
//			for(nindex=0;nindex<set2.size();nindex++)
//			{
//				if(set2[nindex]==temp)
//				{
//					break;
//				}
//			}
//			if(nindex==set2.size())
//			{
//				if(set2.size()<searchnum-1)
//				{
//					set2.push_back(temp);
//				}
//				else
//				{
//					change2++;
//					set2.clear();
//					set2.push_back(temp);
//				}
//			}
//		}
//
//		ofile<<"case #"<<j+1<<":"<<" "<<"change  "<<change<<"  change2:  "<<change2<<endl;
//
//	}
//	ifile.clear();
//	ifile.close();
//	
//	ofile.clear();
//	ofile.close();
//	return 0;
//}
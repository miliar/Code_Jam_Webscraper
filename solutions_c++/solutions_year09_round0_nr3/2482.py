//#include <string>
//#include <iostream>
//#include <fstream>
//#include <sstream>
//#include <vector>
//using namespace std;
//
//
//string search = "welcome to code jam";
//int searchlength = (int)search.size();
//
//void findchar(int c,string *input,int start,int *result);
//int main()
//{
//	int totalline;
//	ifstream infile;
//	infile.open("in");
//    if (!infile) {
//		cerr << "error: unable to open input file: "
//			 << endl;
//	    return -1;
//	}
//	ofstream outfile;
//	outfile.open("out.txt");
//
//	string meta;
//	getline(infile,meta);
//	istringstream stream(meta);
//	stream >> totalline;
//	int *answer = (int*)malloc(sizeof(int)*totalline);
//	for(int i=0; i<totalline;i++)
//	{
//		string temp;
//		getline(infile,temp);
//		int result = 0;
//		findchar(0,&temp,0,&result);
//		cout<<result<<endl;
//		answer[i] = result % 10000;
//	}
//	for (int j=0;j<totalline;j++)
//	{
//		outfile << "Case #"<<j+1<<": " << answer[j]/1000 <<(answer[j]/100)%10 << (answer[j]/10%10)<<(answer[j]%10)<<endl;
//	}
//	infile.close();
//	outfile.close();
//}
//
////find c th element in "search" 
//void findchar(int c,string *input,int start,int *result)
//{
//	for (int k=start;k<(int)(*input).size();k++)
//	{
//		if (search[c]==(*input)[k])
//		{
//			if (c==searchlength-1)
//			{
//				(*result)++;
//			}
//			else
//			{
//				findchar(c+1,input,k+1,result);
//			}
//		}
//	}
//}

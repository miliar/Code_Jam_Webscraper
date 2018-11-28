#include<vector>
#include<map>
#include<set>
#include <iostream>
#include "basetsd.h"
#include <algorithm>
#include "math.h"
#include<string>


using namespace std;

//int getMinutes(char* str){
//	int t=0;
//	t += (int)(str[0]-'0')*600 + (int)(str[1]-'0')*60 + (int)(str[3]-'0')*10 + (int)(str[4]-'0');
//	return t;
//}
//
//struct schedule{
//int mStart;
//int mEnd;
//bool isDone;
//};
//
//void sortVec1(vector<schedule> &ioS)
//{
//	for (int i=0;i<ioS.size();++i)
//	{
//		for (int j=i+1;j<ioS.size();++j)
//		{
//			if (ioS[i].mStart > ioS[j].mStart)
//			{
//				schedule temp = ioS[i];
//				ioS[i] = ioS[j];
//				ioS[j] = temp;
//			}
//		}
//	}
//}
//
//bool GetNextSchedule(vector<schedule>&A,vector<schedule>& B,int& index, int&aOrb)
//{
//	int firstA,firstB;
//
//	firstB = B.size() + 1;
//	firstA = A.size() + 1;
//	
//	for (int i=0;i<A.size();++i)
//	{
//		if (A[i].isDone == false)
//		{
//			firstA = i;
//			break;
//		}
//	}
//	
//	for (int i=0;i<B.size();++i)
//	{
//		if (B[i].isDone == false)
//		{
//			firstB = i;
//			break;
//		}
//	}
//	
//	if (firstA >= A.size() && firstB >= B.size() )
//	{
//		return false;
//	}
//	
//	if (firstA >= A.size())
//	{
//		index = firstB;
//		aOrb = 2;
//		return true;
//	}
//	
//	if (firstB >= B.size())
//	{
//		index = firstA;
//		aOrb = 1;
//		return true;
//	}
//	
//	if (A[firstA].mStart < B[firstB].mStart)
//	{
//		index = firstA;
//		aOrb = 1;
//		return true;
//	}
//	else
//	{
//		index = firstB;
//		aOrb = 2;
//		return true;
//	}
//	
//}
//
//bool GetNextBestTrain(vector<schedule>& A,vector<schedule>&B, int& aOrb, int& currScheduleEnd)
//{
//	int currEnd = currScheduleEnd;
//	int bestTrainIndex;
//	if (aOrb == 1 )
//		bestTrainIndex = A.size()+1;
//	else
//		bestTrainIndex = B.size() + 1;
//	
//
//	if(aOrb == 1)
//	{
//		int maxEnd = 1 << 31;
//		for (int z = 0; z < A.size(); ++z)
//		{
//			if (A[z].isDone == false && A[z].mStart > currEnd)
//			{
//				if (A[z].mEnd < maxEnd)
//				{
//					maxEnd = A[z].mEnd;
//					bestTrainIndex = z;
//				}
//			}
//		}
//		if (bestTrainIndex < A.size())
//		{
//			A[bestTrainIndex].isDone = true;
//			currScheduleEnd = A[bestTrainIndex].mEnd;
//			aOrb = 3 - aOrb;
//			return true;
//		}
//		else
//			return false;
//	}
//
//	if(aOrb == 2)
//	{
//		int maxEnd = 1 << 31;
//		for (int z = 0; z < B.size(); ++z)
//		{
//			if (B[z].isDone == false && B[z].mStart > currEnd)
//			{
//				if (B[z].mEnd < maxEnd)
//				{
//					maxEnd = B[z].mEnd;
//					bestTrainIndex = z;
//				}
//			}
//		}
//		if (bestTrainIndex < B.size())
//		{
//			B[bestTrainIndex].isDone = true;
//			currScheduleEnd = B[bestTrainIndex].mEnd;
//			aOrb = 3 - aOrb;
//			return true;
//		}
//		else
//			return false;
//	}
//
//
//}
//
//int main1()
//{
//int aTrains = 0;
//int bTrains = 0;
//vector<schedule> A,B;
//int nTestCases;
////cin >> nTestCases;
//for (int i=0;i<nTestCases;++i)
//{
//	int nA,nB, turnTime;
//	cin >> turnTime;
//	cin >> nA;
//	cin >> nB;
//	for (int j=0; j<nA;++j)
//	{
//		schedule s;
//		char str[100];
//		cin >> str;
//		s.mStart = getMinutes(str);
//		cin >> str;
//		s.mEnd = turnTime + getMinutes(str);
//		s.isDone = false;
//		A.push_back(s);
//	}
//	for (int j=0; j<nB;++j)
//	{
//		schedule s;
//		char str[100];
//		cin >> str;
//		s.mStart = getMinutes(str);
//		cin >> str;
//		s.mEnd = turnTime + getMinutes(str);
//		s.isDone = false;
//		B.push_back(s);
//	}
//	
//	sortVec1(A);
//	sortVec1(B);
//	int index, aOrb;
//	
//	while (GetNextSchedule(A,B,index,aOrb))
//	{
//		int currScheduleEnd;
//		if (aOrb == 1)
//		{aTrains++; A[index].isDone = true; currScheduleEnd = A[index].mEnd;}
//		else	
//		{bTrains++;B[index].isDone = true; currScheduleEnd = B[index].mEnd;}
//		aOrb = 3 - aOrb;
//		while(GetNextBestTrain(A,B,aOrb,currScheduleEnd));
//	}
//	
//
//}
//
//return 0;
//}
//
//
//void sortVec2(vector<double> &inV)
//{
//	for (int i=0;i<inV.size();++i)
//	{
//		for (int j=i+1;j<inV.size();++j)
//		{
//			if (inV[i]>inV[j])
//			{
//				float temp = inV[i];
//				inV[i] = inV[j];
//				inV[j] = temp;
//			}
//		}
//	}
//}
//
////optimize dot prod
//int main2()
//{
//	int nTestCases;
//	cin >> nTestCases;
//	for (int i=0;i<nTestCases;++i)
//	{
//		int veclen;
//		cin >> veclen;
//		vector<double> x,y;
//		for (int j=0;j<veclen;++j)
//		{
//			double f;
//			cin >> f;
//			x.push_back(f);
//		}
//		for (int j=0;j<veclen;++j)
//		{
//			double f;
//			cin >> f;
//			y.push_back(f);
//		}		
//		sortVec2(x);
//		sortVec2(y);
//		double dotProd = 0;
//		for (int j=0;j<veclen;++j)
//		{
//			dotProd+= x[veclen-j-1]*y[j];
//		}
//		LONG64 z = dotProd;
//		cout << "Case #" << i+1 << ": " << z << "\n";
//	}
//	return 0;
//}
//
//
////optimize num key presses
//int main3()
//{
//
//	int nTestecases;
//	cin >> nTestecases;
//	for (int i=0;i<nTestecases;++i)
//	{
//		int alphaSize, nKeys, maxCharsperKey;
//		cin >> maxCharsperKey;
//		cin >> nKeys;
//		cin >> alphaSize;
//		vector<int> freq;
//		for (int j=0;j<alphaSize;++j)
//		{
//			int fr;
//			cin >> fr;
//			freq.push_back(fr);
//		}
//		sort(freq.begin(),freq.end());
//		LONG64 numKeyPresses = 0;
//		for (int j=0;j<alphaSize;++j)
//		{
//			int orderOnKey = j/nKeys;
//			orderOnKey++;
//			numKeyPresses+=orderOnKey*freq[alphaSize-j-1];
//		}
//		cout << "Case #" << i+1 << ": " << numKeyPresses << "\n";
//	}
//
//return 0;
//}
//
//
//void GetKBaeseRepr(int num, vector<int>& outRepr,int k)
//{
//	while (num != 0)
//	{
//		int dig = num %k;
//		outRepr.push_back(dig);
//		num = num / k;
//	}
//}
//
//
//
//
//float AREA(int x1,int y1,int x2,int y2,int x3,int y3)
//{
//	float f,d12,d23,d13,s;
//	float l12x = x2-x1;
//	float l12y = y2-y1;
//	float l23x =x2-x3;
//	float l23y = y2-y3;
//	float l13x = x3-x1;
//	float l13y = y3-y1;
//	d12 = sqrt(pow(l12x,2)+pow(l12y,2));
//	d23 = sqrt(pow(l23x,2)+pow(l23y,2));
//	d13 = sqrt(pow(l13x,2)+pow(l13y,2));
//	s = (d12+d23+d13)/2.0;
//	f = sqrt(s*(s-d12)*(s-d23)*(s-d13));
//	return f;
//
//}
//
//void GetRelativePoints(vector<int>&ax, vector<int>& ay,vector<int>& tx,vector<int>& ty,
//					   vector<double>& bx,vector<double>& by,int i,int size)
//{
//	for (int j=0;j<size;++j)
//	{
//		bx[j] = ax[j]-ax[i];
//		by[j] = ay[j]-ay[i];
//		tx[j] = ax[j]-ax[i];
//		ty[j] = ay[j]-ay[i];
//	}
//}
//
//
//void ClassifyTriangle()
//{
//	int nTestcases;
//	cin >> nTestcases;
//	double eps = 0.000000;
//	for (int i=0;i<nTestcases;++i)
//	{
//		vector<int> ax(3,0),ay(3,0),tx(3,0),ty(3,0);
//		vector<double> bx(3,1),by(3,1);
//		
//		bool isTriangle = true;
//		cin >> ax[0];
//		cin >> ay[0];
//		cin >> ax[1];
//		cin >> ay[1];
//		if (ax[1]==ax[0] && ay[1] == ay[0])
//		{
//			isTriangle = false;
//		}
//		cin >> ax[2];
//		cin >> ay[2];
//		if ((ax[2]==ax[0] && ay[2] == ay[0])||(ax[1]==ax[2] && ay[1] == ay[2]))
//		{
//			isTriangle = false;	
//		}
//			
//		//remove all cases with triviality
//		if (isTriangle == false)
//		{
//			cout << "Case #"<<i+1<<": "<<"not a triangle\n";
//			continue;
//		}
//		tx=ax;
//		ty=ay;
//		int acute_right_obtuse = 0;
//		int iso_scalane = 1;
//		GetRelativePoints(ax,ay,tx,ty,bx,by,0,3);
//		//Consider if slopes are eual --> colinear  so not a triangle..
//		if (by[1]/by[2] == bx[1]/bx[2])
//		{
//			isTriangle = false;
//			cout << "Case #"<<i+1<<": "<<"not a triangle\n";
//			continue;
//		}
//
//		float zz = (bx[1]*bx[2] + by[1]*by[2])/(sqrt(bx[1]*bx[1] + by[1]*by[1])*sqrt(bx[2]*bx[2] + by[2]*by[2]));
//		if (fabs(0 -zz) <= eps)
//			acute_right_obtuse = 1;
//		if (zz < 0 && zz > -1)
//			acute_right_obtuse = 2;
//		if (fabs(zz-1)<=eps || fabs(zz+1) <= eps )
//		{
//			isTriangle = false;
//			cout << "Case #"<<i+1<<": "<<"not a triangle\n";
//			continue;
//		}
//		//if triangle is not  right and obtuse
//		if (acute_right_obtuse == 0)
//		{
//			tx=ax;ty=ay;
//			GetRelativePoints(ax,ay,tx,ty,bx,by,1,3);
//			zz = (bx[0]*bx[2] + by[0]*by[2])/(sqrt(bx[0]*bx[0] + by[0]*by[0])*sqrt(bx[2]*bx[2] + by[2]*by[2]));
//			if (fabs(0 -zz) <= eps)
//				acute_right_obtuse = 1;
//			if (zz < 0 && zz > -1)
//				acute_right_obtuse = 2;
//			if (acute_right_obtuse == 0)
//			{
//				tx=ax;
//				ty=ay;
//				GetRelativePoints(ax,ay,tx,ty,bx,by,2,3);
//				zz = (bx[0]*bx[1] + by[0]*by[1])/(sqrt(bx[0]*bx[0] + by[0]*by[0])*sqrt(bx[1]*bx[1] + by[1]*by[1]));
//				if (fabs(0 -zz) <= eps)
//					acute_right_obtuse = 1;
//				if (zz < 0 && zz > -1)
//					acute_right_obtuse = 2;
//			}
//		}
//		for (int z=0;z<3;z++)
//		{
//			bx[z] = ax[z]; 
//			by[z] = ay[z];
//		}
//		float len01 = sqrt(pow(bx[1]-bx[0],2)+pow(by[1]-by[0],2));
//		float len12 = sqrt(pow(bx[1]-bx[2],2)+pow(by[1]-by[2],2));
//		float len02 = sqrt(pow(bx[2]-bx[0],2)+pow(by[2]-by[0],2));
//		if (fabs(len01 -len02)<=eps || fabs(len01 -len12)<=eps || fabs(len12 - len02)<=eps)
//		{
//			iso_scalane = 0;
//		}
//		char prop1[100],prop2[100];
//		if (acute_right_obtuse == 0)
//			strcpy(prop2,"acute");
//		else if(acute_right_obtuse == 1)
//			strcpy(prop2,"right");
//		else if (acute_right_obtuse == 2) 
//			strcpy(prop2,"obtuse");
//
//		if (iso_scalane == 0)
//			strcpy(prop1,"isosceles");
//		else if(iso_scalane == 1)
//			strcpy(prop1,"scalene ");
//
//		cout << "Case #"<<i+1<<": "<<prop1<<" "<<prop2<< " "<<"triangle\n";
//	}
//}
//
//
////wrong price  b in GCJ Beta
//void FindMinNumsToBeChangedToGetSortedArr()
//{
//	int nTestcase;
//	cin >> nTestcase;
//	for (int i=0;i<nTestcase;++i)
//	{
//		char temp[100];
//		//string inpStr;
//		vector<string> strvec;
//		vector<int> numVec;
//		vector<bool> isPartOfLIS;
//		int ti=0;
//		
//		string inpStr;
//		getline(cin,inpStr);
//		getline(cin,inpStr);
//		char *pch;
//		
//		pch = strtok ((char*)inpStr.c_str()," ");
//		while (pch != NULL)
//		{
//			string str(pch);
//			strvec.push_back(str);
//			pch = strtok (NULL, " ,.-");
//		}
//
//
//		for (int z=0;z<strvec.size();++z)
//		{
//			int t;
//			cin >>t;
//			numVec.push_back(t);
//			isPartOfLIS.push_back(false);
//		}
//		vector<int> tempvec(numVec.size(),1);
//		vector<int> prevEleIndex(numVec.size(),-1);
//
//		for (int k=1;k<numVec.size();++k)
//		{
//			int curPrev = -1;
//			int curLen = 1;
//			for (int j=0;j<k;++j)
//			{
//				if (numVec[k]>=numVec[j])
//				{
//					if (curLen < tempvec[j]+1)
//					{
//						curLen = tempvec[j]+1;
//						curPrev = j;
//					}
//				}
//			}
//			tempvec[k] = curLen;
//			prevEleIndex[k] = curPrev;
//		}
//		//max index is locn at which longest incr subseq ends.
//		int maxindex = -1;
//		int max = -1;
//		for (int tt=0;tt<tempvec.size();++tt)
//		{
//			if (tempvec[tt] > max)
//			{maxindex = tt;max=tempvec[tt];}
//		}
//
//		while (prevEleIndex[maxindex] != -1)
//		{
//			isPartOfLIS[maxindex] = true;
//			maxindex = prevEleIndex[maxindex];
//		}
//		isPartOfLIS[maxindex] = true;
//		
//		string strtemp;
//		map<string,int> mp;
//		for (int tt=0;tt<isPartOfLIS.size();++tt)
//		{
//			if (isPartOfLIS[tt]==false)
//			{
//				mp[strvec[tt]] = tt;
//			}
//		}
//		map<string,int>::iterator it;
//		for (it=mp.begin();it!=mp.end();++it)
//		{
//			strtemp += it->first;
//			strtemp += string(" ");
//		}
//		string inS;
//		for (int z=0;z<strvec.size();++z)
//		{
//			inS+=strvec[z];
//			inS+=string(" ");
//		}
//
//		cout << inS.c_str()<<"\n";
//		for (int z=0;z<numVec.size();++z)
//		{
//			cout<<numVec[z]<<"     ";
//		}
//		cout<<"\n";
//		cout << "Case #"<<i+1<<": "<<strtemp.c_str()<<"\n\n";
//		
//	}
//}

void GetSetIntersection(set<string>& currInd,set<string>& indSet,set<string>& newInd)
{
	newInd.clear();
	set<string>::iterator it1,it2;
	for (it1=currInd.begin();it1!=currInd.end();++it1)
	{
		if (indSet.find(*it1)!=indSet.end())
		{
			newInd.insert(*it1);
		}
	}
}


//QualRound 1
void QualRound1()
{
	int nTestacase;
	int D,L;
	cin >> L;
	cin >> D;
	cin >>nTestacase;
	string inpStr;
	getline(cin,inpStr);

	set<string> allWords;
	for (int i=0;i<D;++i)
	{
		getline(cin,inpStr);
		allWords.insert(inpStr);
	}
	for (int i=0;i<nTestacase;++i)
	{
		string pat;
		getline(cin,pat);
		vector<set<char> > tokVec;
		int j=0;
		while (j < pat.size())
		{
			if (isalpha(pat[j]))
			{
				set<char> s;
				s.insert(pat[j]);
				tokVec.push_back(s);
				j++;
				continue;
			}
			else 
			{
				j++;
				set<char> s;
				while (pat[j] != ')') 
				{
					s.insert(pat[j]);
					j++;
				}
				tokVec.push_back(s);
				j++;
			}
		}
		set<string> indSet = allWords;

		if(tokVec.size()== L)
		{
			for (int z=0;z<tokVec.size();++z)
			{
				set<char> s = tokVec[z];
				set<char>::iterator it;
				set<string> currInd;
				for (it=s.begin();it!=s.end();++it)
				{
					char c= *it;
					
					set<string>::iterator strIt;
					for (strIt=indSet.begin();strIt!=indSet.end();++strIt)
					{
						if ((*strIt)[z]==c)
						{
							currInd.insert(*strIt);
						}
					}

				}
				set<string> newInd;
				GetSetIntersection(currInd,indSet,newInd);
				indSet = newInd;
				if (indSet.size() == 0)
				{
					break;
				}
			}
		}

		cout << "Case #"<<i+1<<": "<<indSet.size()<<"\n";
		
	}
}


int main()
{
	QualRound1();
	return 0;
}
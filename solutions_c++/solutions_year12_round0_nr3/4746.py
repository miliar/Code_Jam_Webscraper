#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

//int sortednum(int num)
//{
//
//	unsigned int count[10]={0};
//
//	int i = num;
//	unsigned int k=0;
//
//	int output = 0;
//
//	
//
//	while(i!=0)
//	{
//
//
//		count[(i%10)]++;
//		i= i/10;
//
//
//	}
//
//	for(i=9;i>=0;i--)
//	{
//		while(count[i])
//		{
//			output = output*10 + i;
//			
//			count[i]--;
//
//
//		}
//
//	}
//
//	return output;
//}

int powerof10(int n)
{
	int num =1;
	for(int i=0;i<n;i++)
		num = num*10;

	return num;

}

void boringnumber(map<int,int> &m, int n,int A, int B)
{

	int numdigits = 0;
	int temp = n;

	while(temp)
	{
		temp = temp/10;
		numdigits++;

	}
	//cout<<"numdigits"<<numdigits<<endl;
	int i = numdigits;
	temp = n;
	int num;

	map<int,int>::iterator it;
	set<int> myset;
	//myset.insert(n);
	while(i>1)
	{

		num = temp/powerof10(numdigits-1);
		temp = temp % powerof10(numdigits-1);
		temp = (temp*10)+num;

		if(n == temp)
		{
			i--;
			continue;
		}

		
		if(temp<=B&&temp>=A)
		{

			myset.insert(temp);
			it = m.find(temp);

			if(it != m.end())
	
				return;

		}

		i--;

	}


	    if(myset.size()>= 1)
		{

          if(myset.size()==1)
		   m.insert(std::pair<int,int>(n,1));
		  else
		  {
			  int x = myset.size();

			  m.insert(std::pair<int,int>(n,(x*(x+1)/2)));

		  }


		}



}

int main()
{


  //cout << sortednum(1234) <<endl;
  //cout << sortednum(404) <<endl;

	//set<int> ms;

	//for(int i=0;i<10;i++)
	//	ms.insert(1123);

 //cout << ms.size() <<endl;

  ifstream rdfile;
  std::ofstream ofile("output.txt");

  rdfile.open("C-small-attempt1.in");
  
  int count;
  int ic = 0, A,B;


  rdfile >> count;



  while (ic!=count)
  {
	  int i;
	  std::vector<int> c;
	  int repeats = 0;
	  map<int,int> m;
      map<int,int>::iterator  mit;

	  rdfile >> A >> B;

	  //cout<<A<<" "<<B<<endl;

	  for(i=A;i<=B;i++)
	  {
		 //   int num = sortednum(i);
			//if(num == 2210)
			//	cout<<num<<"org"<<i<<endl;
		 //   mit = m.find(num);
		 //   if(mit == m.end())
			// m.insert(pair<int,int>(num,0));
			//else
			//	mit->second++;

		  boringnumber(m,i,A,B);
	  }
	  //cout<<" converted"<<endl;

	  //cout<<m.size()<<endl;
	  c.reserve(m.size());

	  mit = m.begin();
	  while (mit!= m.end())
	  {
		  if((mit->second))
		  c.push_back(mit->second);

		  //if(mit->second == 3)
			 // cout<<mit->first << " sec: "<<mit->second <<endl;

		  mit++;
	  }
	  
	  for( i=0;i<c.size();i++)
	  {
		  repeats = repeats + c[i];
		  //cout<<c[i]<<endl;

	  }
	  //cout<<c.size()<<endl;
	  ofile<<"Case #"<<ic+1<<": "<<repeats<<endl;
	  ic++;
  }


  cin.get();
  return 1;
}

#include <iostream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

void main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);

	//creating the map
	//*********************************************************************8
	map<string,string> mymap;
	string AlienString ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string RealString = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	string AlienL,RealL;
	map<string,string>::iterator founds;
	pair<map<string,string>::iterator,bool> ret;

	mymap.insert(pair<string,string> ("z","q"));
	mymap.insert(pair<string,string> ("q","z"));

	//inserting the letter mapping into a map
	for(int i=0;i<AlienString.size();i++)
	{

		AlienL=AlienString[i];
		RealL=RealString[i];
		founds=mymap.find(AlienL);
		if(founds!=mymap.end())
		{
			//Do nothing
			//For Debugging purpose (couting)
			//cout<<"the letter was there -- "<<founds->first<<"--"<<founds->second<<endl;
		}
		else
		{
			mymap.insert(pair<string,string> (AlienL,RealL));
			//mymap.insert(pair<string,string> (RealL,AlienL));
		}

	}
	//*****************************************************************

	//For Debugging purpose (couting)
	/*for(founds=mymap.begin(); founds!=mymap.end(); ++founds)
	{
		cout<<(*founds).first<<"  :  "<<(*founds).second<<endl;
	}*/
	

	//Now to take the input and analyze
	int T=0;
	int ws;
	string Inputline;
	string InputL;


	cin >> T;
	getline(cin,Inputline);	
	for(int i=1;i<=T;i++)
	{
		string result="";
		//cout<<"enter your line of code"<<endl;
		//cin>>Inputline;
		getline(cin,Inputline);	
		//cin>>ws;
		//cout << "Case #" <<i<<": ";
		for(int j=0;j<Inputline.size();j++)
		{
			InputL=Inputline[j];
			founds=mymap.find(InputL);
			if(founds!=mymap.end())
			{
				//cout<<founds->second;
				//result.insert(founds->second);
				result+=founds->second;
			}

		}
		//cout<<endl;
		cout << "Case #" << i << ": " << result << endl;


	}


	//system("Pause");
}
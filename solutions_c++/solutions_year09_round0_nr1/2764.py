#include <iostream>
#include <vector>
#include <string>

int length;
int dictionary_length;
int casenumbers;

using namespace std;

class alienlang{
public:
	int compare();
	void putin(string tempstring);
	void newcase();
	vector<string> dictionary;
private:
	vector<string> casecompare;
	bool comparingfunc(int a);
	
};

bool littlecompare(string big, string one)
{
	//cout <<"Entering Little Compare; big is: "<<big<<" small is: " <<one <<endl;
	char temp=one[0];
	for(int i=0;i<big.size();i++)
	{
		if(temp==big[i]) 
		{
			//cout <<"Yes, there is a comparison" <<endl;
			return true;
		}
	}
	//cout <<"False!None" <<endl;
	return false;
}

bool alienlang::comparingfunc(int a){
	string dicside=dictionary[a];
	//cout << "Comparing: " <<dicside <<endl;
	for(int i=0;i<length;i++)
	{
		//cout <<"Minicomparing: " <<casecompare[i] <<" with " <<dicside.substr(i,1) <<endl;
		if(casecompare[i].size()==1){
			if(casecompare[i]!=dicside.substr(i,1)) return false;
		}
		else
		{
			if(littlecompare(casecompare[i],dicside.substr(i,1))==false) return false;
		}
	}
	return true;
}

int alienlang::compare(){
	int returnval=0;
	for(int a=0;a<dictionary_length;a++)
	{
		//cout <<"Comparing the word " <<dictionary[a] <<endl;
		if(comparingfunc(a)==true)
		{
			returnval++;
			//cout << "It's the same!" <<endl;
		}
		//else cout <<"NOT THE SAME!" <<endl;
	}
	return returnval;
}

void alienlang::newcase(){
	vector<string> empty;
	casecompare=empty;
}

void alienlang::putin(string tempstring){
	string enteringstring;
	for(int i=0;i<length;i++)
	{
		//cout <<"Iteration  is: " <<i <<" tempstring is: " <<tempstring <<endl;
		if(tempstring.substr(0,1)=="("){
			int endval=0;
			bool stayinloop=true;
			while(stayinloop){
				endval++;
				if(tempstring.substr(endval,1)==")") stayinloop=false;
			}
			enteringstring=tempstring.substr(1,endval-1);
			//cout <<"Entering string is: " <<enteringstring <<endl;
			casecompare.push_back(enteringstring);
			tempstring.erase(0,endval+1);
		}
		else{
			enteringstring=tempstring.substr(0,1);
			//cout <<"Entering string is: " <<enteringstring <<endl;
			casecompare.push_back(enteringstring);
			tempstring.erase(0,1);
		}
	}
}

int main()
{
	alienlang cases;
	alienlang empty;
	cases.newcase();
	empty.newcase();
	cin >> length;
	cin >> dictionary_length;
	cin >> casenumbers;
	string tempstring;
	for(int i=0;i<dictionary_length;i++)
	{
		cin>>tempstring;
		cases.dictionary.push_back(tempstring);
	}
	cin.ignore();
	for(int i=1;i<=casenumbers;i++)
	{
		cases.newcase();
		cout <<"Case #"<<i<<": ";
		getline(cin,tempstring);
		cases.putin(tempstring);
		cout <<cases.compare()<<endl;
	}
	return 0;
}

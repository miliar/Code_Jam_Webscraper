#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

using namespace std;
#define iMAX 0xfffffff
void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

vector<int>  getDigit(int num, int base)
{
	vector<int>  dig;
	int t = num  ;
	//cout << "\n num:" << num << " base: " << base << " dig: ";

	while (t >= 1){
		int s = t % base ;
		t = t / base ; 
		dig.push_back(s);
		//cout << " " << s ; 
	}
	//cout << "dig size(): " << dig.size() ;	
	return dig ;
	
}
void apendset(set<int> &a, set<int> &b)
{
				for(set<int>::iterator it = b.begin();
					it != b.end() ;
					it ++){
					a.insert(*it);
				}
}
bool inVector(int a , vector<int> &v){
	for(int i =0; i < v.size()  ; i ++){
		if(a == v[i])
			return true;
	}

	return false ; 
}
bool inSet(int a,set<int> &s)
{
	if(s.find(a) != s.end()){
		return true;
	}
	return false;
} 	
bool inorder(string& st)
{
	char t = st[0];
	for(int i =1; i < st.size() ; i ++){
		if(t >= st[i]){
			t = st[i];
		}else{
			return false;
		}
	}
	return true;
}
int c_compare (const void * a, const void * b)
{
  return ( *(char*)a - *(char*)b );
}

void isort(string &str){
	char buf[2048];
	sprintf(buf,"%s",str.c_str());
	 qsort (buf, str.size(), sizeof(char), c_compare);
	str = string(buf);
}

string mswitch(char c, string sub)
{
	string ns;
	//cout <<"\nmswitch on:" << c << " , sub:" << sub ;
	if(sub.size() == 1){
		ns = sub + c;
		return ns;
	}else{
		//find the min c but > c
		for(int  p = 1 ; p < '9' - c + 1; p ++){
			char d = c + p;
		
			if(sub.find(d) == string::npos){
				//cout << "\n can not find:" << d ; 
				continue;
			}else{
				int k = sub.find(d);
				//cout << "\nfind " << d << " at pos :" << k << " in sub:" << sub ;
				sub[k] = c ; 
				//cout <<"\nreplaced sub:" << sub ;
				isort(sub);
				//cout <<"\nsorted sub:" << sub ;
				ns = d + sub;
				//cout <<"\nns:" << ns ;
				return ns;
			};
			if(p == '9' - c + 1) {
				cout << "\nERROR" ;
			}
		}
	}
	return 0;
}
void iswitch(string & num){
	int size = num.size() ;
	for(int i = size-2 ; i >=0 ; i --)
	{
		string sub = num.substr(i,2);
		//cout << "\nsub:" << sub;
		if(inorder(sub)){
		}else{
			string newst=mswitch(num[i],num.substr(i+1));
			num = num.substr(0,i) + newst;
			return ;
		}
	}	
	//all inorder
	char c='0';
	string newst = mswitch(c,num);
	num = newst ;
	return ;
}
int main(int argc, char** argv){
  string line;
  ifstream myfile (argv[1]);
  if (myfile.is_open())
  {
	int t; 
	getline(myfile,line);
	t = atoi(line.c_str());
	//cout << "\n" << t; 
    for(int i = 0 ; i < t ; i ++)
    {
      getline (myfile,line);
      //cout << "\n" << line << " size: " << line.size() ;
      iswitch(line);
      cout << "Case #" << i+1 << ": " << line << endl;
      
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

}

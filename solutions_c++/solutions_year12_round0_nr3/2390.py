#include<iostream>
#include<string>
#include<fstream>
#include<hash_map>
#include<map>
using namespace std;

string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0; i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}
int num_pair(int A, int B){
	map<string,int> pair_map;

	if(A>B) return -1;
	string a,b;
	a = convertInt(A);
	b = convertInt(B);
	if(a.length() != b.length())  return -1;
	int count = 0;
	for(int t = A; t<=B ; t++){
		//check if t is possible
		string string_t = convertInt(t);
		for (int j = 1 ; j<string_t.length();j++){
			string new_string = string_t.substr(j,string_t.length()-j)+string_t.substr(0,j);
			int new_num = atoi(new_string.c_str());
			if(new_num>=A && new_num<=B && new_num !=t){
				count++;
			//	cout<<new_string<<" "<<string_t<<endl;
				string to_map = new_string+" "+string_t;
				pair_map[to_map]=1;
			}
		}
	}
	return pair_map.size()/2;
}

int main(){
	ifstream fin;
		fin.open("C.in");
		ofstream fout;
		fout.open("C.out");
		int case_num;
		fin>>case_num;
		int A;
		int B;
		for(int t  = 0; t < case_num; t++){
			fin>>A>>B;
            cout<<t<<endl;
			fout<<"Case #"<<t+1<<": "<<num_pair(A,B)<<endl;
		}
		fin.close();
		fout.close();

		return 0;
}

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

struct data{
	string dep;
	string arr;
	char st;
};



bool compare (const data& lhs, const data& rhs){
	if(lhs.dep < rhs.dep)
		return true;
	else if(lhs.dep == rhs.dep && lhs.arr < rhs.arr) 
		return true;
	else 
		return false;
}

string addMinutes(string q, int min){
	long a = strtol(q.substr(0,2).c_str(), NULL, 10);
	long b = strtol(q.substr(3,2).c_str(), NULL, 10);
	b += min;
	if(b >= 60){
		a++; b = b - 60;
	}
	b = b % 60;
	if(a>=24) return "30:00";
	char temp[3]; string t;
	sprintf(temp, "%d:", a);
	t = temp;
	if (t.length() == 2)
		t = "0" + t;
	string s;
	sprintf(temp, "%d", b);
	s = temp;
	if (s.length() == 1)
		s = "0" + s;	
	return (t + s);
}
typedef priority_queue<string, vector<string>, greater<string> > mypq;

int main(){
	mypq t_a, t_b;
	string arr, dep;
	data temp;
	vector<data> list_a;
	int N,T,A,B;
	int a, b;
	vector<data>::iterator it;
	
	cin >> N;
	for(int I = 1; I <= N; I++){
		cin >> T >> A >> B;
		list_a.clear();
		for(int i = 0; i < A; i++){
			cin >> dep >> arr;
			temp.dep = dep; temp.arr = arr; temp.st = 'a';
			list_a.push_back(temp);
		}
		
		for(int i = 0; i < B; i++){
			cin >> dep >> arr;
			temp.dep = dep; temp.arr = arr; temp.st = 'b';
			list_a.push_back(temp);
		}
		sort(list_a.begin(), list_a.end(), compare);
		while(!t_a.empty()) t_a.pop();
		while(!t_b.empty()) t_b.pop();
		a = 0; b = 0;
		for(it = list_a.begin(); it != list_a.end(); it++){
			temp = *it;
			if(temp.st == 'a'){
				if(t_a.empty() || t_a.top() > temp.dep){
//					cout<<"Here: "<<t_a.top()<<" "<<temp.dep<<endl;
					a++;
					t_b.push(addMinutes(temp.arr, T));
				}
				else{
					t_a.pop();
					t_b.push(addMinutes(temp.arr, T));
				}
			}
			else if(temp.st == 'b'){
				if(t_b.empty() || t_b.top() > temp.dep){
					b++;
					t_a.push(addMinutes(temp.arr, T));
				}
				else{
					arr = t_b.top();
					t_b.pop();
					t_a.push(addMinutes(temp.arr, T));
				}
			}
		}
		cout <<"Case #"<<I<<": "<<a<<" "<<b<<"\n"; 
	}
	return 0;
}
		

			
			
		
	
	
	
	

	
	


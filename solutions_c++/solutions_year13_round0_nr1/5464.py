#include <iostream>
//#include <map>  
//#include <vector>
#include <set>  
#include <string>
#include <string.h>
#include <fstream>
//#include <algorithm>  

using namespace std;

int n,m,count1;
int calcmap[10][10][40]={0};
int ccount[10]={0};
char fn[26]="count/documents/1.txt";

//map<string,int> fnc;
//vector<string> fstr;
//set<string> stop;
//vector<pair<string,int> > tVector;  
char map[16];

/*int index(string s){
	int i;
	for(i=0;i<40;i++){
		if(s.compare(feature[i])==0)return i;
	}
	return -1;
}*/

/*int cmp(const pair<std::string, int>& x, const pair<std::string, int>& y){  
	return x.second > y.second;  
}  
   
void sortMapByValue(map<std::string, int>& tMap, vector<std::pair<std::string, int> >& tVector){  
	for(map<string, int>::iterator curr = tMap.begin(); curr != tMap.end(); curr++){  
		tVector.push_back(make_pair(curr->first, curr->second));  
	}  
   
	sort(tVector.begin(), tVector.end(), cmp);  
}  

vector<string> split(const string& src, string separate_character)
{
    vector<string> strs;
    int separate_characterLen = separate_character.size();//分割字符串长度，这样就可以支持多字 符串的分隔符
    int lastPosition = 0, index = -1;
    while (-1 != (index = src.find(separate_character, lastPosition)))
    {
        strs.push_back(src.substr(lastPosition, index - lastPosition));
        lastPosition = index + separate_characterLen;
    }
    string lastString = src.substr(lastPosition);
    if (!lastString.empty())
    strs.push_back(lastString);
    return strs;
}



void printSet(set<string> s)
{
	copy(s.begin(), s.end(), ostream_iterator<string>(cout, ", ") );
	cout<<endl;
}


*/

int judge(int i){
	int flag=1;
	int row=i/4;
	int col=i%4;
	int c=i;
	int count=0;
	int j=0;
	
	while(c-1>=0&&(--c)/4==row){
		if(map[c]!=map[i])break;
		count++;
	}
	c=i;
	while(c+1<16&&(++c)/4==row){
		if(map[c]!=map[i])break;
		count++;
	}
	if(count==3)return 1;
	c=i;count=0;
	while(c-4>=0){
		c-=4;
		if(map[c]!=map[i])break;
		count++;
	}
	c=i;
	while(c+4<16){
		c+=4;
		if(map[c]!=map[i])break;
		count++;
	}
	if(count==3)return 1;
	return 0;
}

int judgeRe(){
	for(int j=0;j<16;j++){
		char f;
		int j1,count=0;
		if(map[j]=='T'){
			int row=j/4;
			int col = j%4;
			for(int j1=0;j1<4;j1++){
				if(j1!=col){f=map[row*4+j1];break;}
			}
			for(j1=0;j1<4;j1++){
				if(map[row*4+j1]==f)count++;
			}
			if(count==3){
				if(f=='X'){return 1;}
				else if(f=='O'){return 2;}
			}
			count=0;
			for(j1=0;j1<4;j1++){
				if(j!=row){f=map[j1*4+col];break;}
			}
			for(j1=0;j1<4;j1++){
				if(map[j1*4+col]==f)count++;
			}
			if(count==3){
				if(f=='X'){return 1;}
				else if(f=='O'){return 2;}
			}
			int xc=0,oc=0;
			if(j==0||j==5||j==10||j==15){
				for(j1=0;j1<4;j1++){
					if(map[j1*5]=='X'){xc++;}
					else if(map[j1*5]=='O'){oc++;}
				}
				if(xc==3)return 1;
				if(oc==3)return 2;
			}
			xc=0;oc=0;
			if(j==3||j==6||j==9||j==12){
				for(j1=1;j1<=4;j1++){
					if(map[j1*3]=='X'){xc++;}
					else if(map[j1*3]=='O'){oc++;}
				}
				if(xc==3)return 1;
				if(oc==3)return 2;
			}
		}
		if(judge(j)){
			if(map[j]=='X'){return 1;}
			else if(map[j]=='O'){return 2;}
		}
	}
	if(map[5]==map[0]&&map[10]==map[0]&&map[15]==map[0]){
		if(map[0]=='X'){return 1;}
		else if(map[0]=='O'){return 2;}
	}
	if(map[6]==map[3]&&map[9]==map[3]&&map[12]==map[3]){
		if(map[3]=='X'){return 1;}
		else if(map[3]=='O'){return 2;}
	}
	return 0;
}

void main() {
    int t=0,i1=0,s,n,p;
	int pointc = 0,c=0;
	string word1,word2,filename;
	string lines;
	count1=0;
	ifstream in("D:\\Program Files\\Microsoft Visual Studio\\MyProjects\\poj\\A-small-attempt1.in");
	//cout<<-1/4<<endl;
	ofstream examplefile ("test.txt");//count/test.txt
	if(in && examplefile.is_open()){
		//getline (in, lines);
		in>>count1;
		cout<<count1<<endl;
		getline (in, lines);
		for(int i4=0;i4<count1;i4++){
			pointc=0;
			for(i1=0;i1<4;i1++){
				getline (in, lines);
				//cout<<lines.size()<<endl;
				for(int j=0;j<4;j++){
					//cout<<lines.at(j);
					map[i1*4+j]=lines.at(j);
					if(lines.at(j)=='.')pointc++;
					cout<<map[i1*4+j]<<" ";
				}
				
				cout<<endl;
			}
			examplefile<<"Case #"<<++t<<": ";
			if(judgeRe()==1){
				cout<<"X win"<<endl;
				examplefile<<"X won"<<endl;
			}else if(judgeRe()==2){
				cout<<"O win"<<endl;
				examplefile<<"O won"<<endl;
			}else{
				if(pointc==0){
					cout<<"Draw"<<endl;
					examplefile<<"Draw"<<endl;
				}else{
					cout<<"not over"<<endl;
					examplefile<<"Game has not completed"<<endl;
				}
				
			}
			/*for(i1=0;i1<16;i1++){
			
				cout<<map[i1];	
			
			}	cout<<endl;*/
			getline (in, lines);
			/*in>>n>>s>>p;
			cout<<"n:"<<n<<" s:"<<s<<" p:"<<p<<endl;
			for(i1=0;i1<n;i1++){
				in>>map[i1];
			}
			less_s = p*3-4;
			if(p==1)less_s=-1;
			if(p==0)less_s=-2;
			c=0;
			for(i1=0;i1<n;i1++){
				if(map[i1]==less_s||map[i1]==less_s+1){
					if(s!=0&&p!=1){
						s--;c++;
					}
				}else if(map[i1]>less_s+1){
					c++;  
				}
				//cout<<map[i1]<<" ";
			}*/
			
			//cout<<"c:"<<c<<endl;
		//	cout<<endl;
		}
	/*	while(getline (in, lines)){  // have no '\n',
			
		
//			cout<<lines<<" "<<lines.size()<<endl;
//			examplefile<<"Case #"<<t++<<": ";
//			for(int i4=0;i4<lines.size();i4++){
//				
//			}
			examplefile<<endl;
	
			//break;
			 // ;
			// store the lines to a vector or list, use method insert
		}*/
		// ...
	}else{
		// open file fail....
	} 
	in.close();
	examplefile.close();

	/*ofstream examplefile ("count/本.txt");
	if(examplefile.is_open()) {
		examplefile << "This is a line.\n";
		examplefile << "This is another line.\n";
		examplefile.close();
	}*/
	
   // return 0;
}

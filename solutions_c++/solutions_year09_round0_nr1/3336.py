#include <fstream>
#include <stack>
#include <string>
using namespace std;

int main(){
 int l,d,n;
 fstream in("in.txt");
 fstream out("out.txt");
in>>l>>d>>n;
int i;
//scanf("\n");
string words[6000],tests[500];
getline(in,words[0]);
for (i=0;i<d;i++){
 getline(in,words[i]);
}
for (i=0;i<n;i++){
 getline(in,tests[i]);
}

int step=-1;
int g=0;
int flag=0;
int res=0;
stack <char> ls[15],cur;
for (i=0;i<n;i++){
     res=0;
	 step=-1;
	 flag=0;
    //заполним стек
	 for (g=0;g<l;g++){
		 while(!ls[g].empty()){
		  ls[g].pop();
		 }
	 }
	 for (g=0;g<tests[i].length();g++){
		if (tests[i][g]=='('){
		 step++;
		 flag=1;
		 continue;
		}
		if (tests[i][g]==')'){
		 flag=0;
		 continue;
		}
       if(flag)
		   ls[step].push(tests[i][g]);
	   else{
		   step++;
		   ls[step].push(tests[i][g]);
	   }
	}
	int k;
	for(g=0;g<d;g++){
		//int ok=1;
		//letters check
		for (k=0;k<l;k++){
    	 flag=0;
		 cur=ls[k];
		 while (!cur.empty()){
			 if (cur.top()==words[g][k]){
				 flag=1;
				 break;
			 }
			 cur.pop();
		 }

		 if(!flag)
			 break;
		 if (k==l-1){
		  if(flag)
			  res++;
		 }
		}
	}


	out<<"Case #"<<i+1<<": "<<res<<endl;
}

return 0;
 }
#include <iostream>
#include <stack>
using namespace std;
int inttochar[10]={' ','A','S','D','F','Q','W','E','R'};
int change[130][130]={0},die[100]={0},die2[100]={0},ntc,strck[131];

int main(){
    cin >> ntc;
    for(int tc=1;tc<=ntc;tc++){
        memset(change,0,sizeof(change));
        memset(die,0,sizeof(die));
        memset(strck,0,sizeof(strck));
        int c,d,n;
        cin >> c;
        for(int i=1;i<=c;i++){
              char s1,s2,s3;
              cin >> s1 >> s2 >> s3;
              change[int(s1)][int(s2)]=int(s3);
              change[int(s2)][int(s1)]=int(s3);
        }
        cin >> d;
        for(int i=1;i<=d;i++){
              char s1,s2;
              cin >> s1 >> s2;
              die[i]=int(s1);
              die2[i]=int(s2);
        }
        stack <int> arr; 
        cin >> n;
        for(int i=1;i<=n;i++){
              char s1;
              cin >> s1 ;
              if(arr.empty())
                 arr.push(int(s1)),strck[s1]=1;
              else
              {
                 if(change[arr.top()][s1]!=0){
                    int tmp = arr.top();
                    strck[tmp]--;
                    arr.pop();
                    strck[change[tmp][s1]]++;
                    arr.push(change[tmp][s1]);
                 }
                 else
                   arr.push(s1),strck[s1]++;
             /*    for(int j=1;j<=130;j++)
                    if(strck[j])
                       cout << char(j) << " ";
                       cout << endl;*/
                 for(int j=1;j<=d;j++){
                  // cout << char(die[j]) <<" " << char(die2[j]) << endl;
                   if(strck[die[j]] && strck[die2[j]]){
                        while(!arr.empty())
                          arr.pop();
                        memset(strck,0,sizeof(strck));
                        break;
                   }
                 }
                 
                 
              }              
             
        }
        stack <int> ans; 
        while(!arr.empty()){
            ans.push(arr.top());
            arr.pop();
        }
        cout << "Case #"<<tc<<": [";
        if(!ans.empty()){
        cout << char(ans.top());
        ans.pop();
        }
        while(!ans.empty()){
          cout << ", "<<char(ans.top());
          ans.pop();
        }
        cout << "]"<< endl;
    }
}

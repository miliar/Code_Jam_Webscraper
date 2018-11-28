#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
void LabelRefer(vector<string> &words,string &word,vector<string> &referList,int charN);
void ResetRefer(vector<string> &referList,int ReferN,int ReferL);
int FindWordNum(vector<string> &referList,int referL);
int main()
{
    ifstream input;
    ofstream output;

    string inFileName,outFileName;
    cout<<"Please input the input file's location:"<<endl;
    cin>>inFileName;
    cout<<"Please input the output file's location:"<<endl;
    cin>>outFileName;
    input.open(inFileName.data());
    output.open(outFileName.data());

    int L,N,D,result=0;
    vector<string> words;
    //to record all the words
    string word;
    vector<string> referList;
    //to record the refer to a word of letters
    input>>L>>D>>N;
    for (int i=0;i<D;i++){
        input>>word;
        words.push_back(word);
    }
    for (int i=0;i<N;i++){
        input>>word;
        ResetRefer(referList,D,L);
        //Reset the ReferList
        LabelRefer(words,word,referList,L);
        //Label the letter on the word list
        output<<"Case #"<<(i+1)<<": "<< FindWordNum(referList,L) <<endl;
    }
    input.close();
    output.close();
    cout<<"result has been saved!"<<endl;
    return 0;
}
void LabelRefer(vector<string> &words,string &word,vector<string> &referList,int charN){
    vector<string> wordRefer;
    string subword;
    for (int i=0;i<word.length();i++){
        if (word[i]!='('){
            subword.assign(&word[i]);
            subword=subword.substr(0,1);
            wordRefer.push_back(subword);
        }
        else{
            int subStart=word.find_first_of('(');
            int subEnd=word.find_first_of(')');
            subword = word.substr(subStart+1,subEnd-subStart-1);
            wordRefer.push_back(subword);
            word[subStart]='!';
            word[subEnd]='!';
            i=subEnd;
        }
    }
    for (int i=0;i<words.size();i++){
         for(int j=0;j<charN;j++){
             if( wordRefer[j].find( words.at(i)[j] )!= string::npos )
             referList.at(i)[j]='b';
         }
    }
}
void ResetRefer(vector<string> &referList,int referN,int referL){
    referList.clear();
    string word("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
    for (int i=0;i<referN;i++){
        word=word.substr(0,referL);
        referList.push_back(word);
    }
}
int FindWordNum(vector<string> &referList,int referL){
    string word("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb");
    int result=0;
    word=word.substr(0,referL);
    for(int i=0;i<referList.size();i++){
        if (referList.at(i)==word)
        result++;
    }
    return result;
}

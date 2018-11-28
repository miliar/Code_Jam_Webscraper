#include<iostream>
#include<vector>


using namespace std;

class Sequence{
    vector<char> seq;
    int index;
    
    public:
    void insertSeq(char color);
    char getCurrent();
    void currentOver();
};

void Sequence::insertSeq(char color){
	seq.push_back(color);
}

char Sequence::getCurrent(){
	return seq.at(index);
}

void Sequence::currentOver(){
	index++;
}

class Robot{
    char color;
    vector<int> buttons;
    int index;
    int position;
    Sequence * seq;
    
    public:
    
    Robot(char color,Sequence * seq){this->color=color;this->seq=seq;index=0;position=1;}
    
    void addButton(int n){buttons.push_back(n);}
    
    int currentButton(){return buttons.at(index);}
    
    int makeMove();
};

int Robot::makeMove(){
 	if(currentButton()==-1)
 	 	return 0;
    if(position>currentButton()){
        position--;
    }else if(position<currentButton()){
        position++;
    }else{
        if(this->color == seq->getCurrent()){
           //seq->currentOver();
           this->index++;
           return 1;
        }
    }
    return 0;
}



int main(int argc,char *argv[]){
    
    Sequence *seq;
    Robot * orangeBot, * blueBot;
    int t,n;
    char color;
    int button;
    int clock;
    
    cin>>t;
    
    for(int i=0;i<t;i++){
        cin>>n;
        
        seq = new Sequence();
        orangeBot=new Robot('O',seq);
        blueBot=new Robot('B',seq);
        clock=0;
        
        for(int j=0;j<n;j++){
            cin>>color>>button;
            seq->insertSeq(color);
            if(color=='O')
              orangeBot->addButton(button);
            else
              blueBot->addButton(button);
            
        }
        seq->insertSeq('E');
        orangeBot->addButton(-1);
        blueBot->addButton(-1);
        
        while(seq->getCurrent()!='E'){
        	//debut
        	//cout<<"bug\n";
        	clock++;
        	int otrue=orangeBot->makeMove();
        	int btrue=blueBot->makeMove();
        	if(otrue || btrue){
        		seq->currentOver();
        	}
        }
        
        cout<<"Case #"<<i+1<<": "<<clock<<endl;
        delete orangeBot;
        delete blueBot;
        delete seq;
    }
    
}


#include <iostream>
#include <vector>
#include <string>
#include <queue>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::queue;

class Bot{
public:
	Bot(): position (1){}

	//devuelve true si ejecuto la accion
	bool work(){
		if ( position == commands.front() ){
			//hacer push
			commands.pop();
			return true;
		}
		free();
		return false;
	}

	void free(){
		if ( !commands.empty() ){
			if ( commands.front() > position ) {
				position++;
			} else if ( commands.front() < position ){
				position--;
			}
		}
	}

	queue<int> commands;
	int position;
};

int main(){


	int N;
	cin>>N;

	for ( int n=1; n<=N; n++){

		Bot B;
		Bot O;
		queue<char> cmds;

		int S;
		cin>>S;
		for ( int s=0; s<S; s++){
			char bot;
			int t;
			cin>>bot;
			cin>>t;
			cmds.push(bot);
			if ( bot == 'O')
				O.commands.push( t );
			else
				B.commands.push( t );
		}

		//simular

		int steps = 0;

		while( !cmds.empty() ){
			bool buttonPushed = false;
			if ( cmds.front() == 'O'){
				buttonPushed = O.work();
				B.free();
			} else {
				buttonPushed = B.work();
				O.free();
			}

			if ( buttonPushed )
				cmds.pop();

			steps++;
		}

		cout<<"Case #"<<n<<": "<<steps<<endl;
	}

	return 0;
}

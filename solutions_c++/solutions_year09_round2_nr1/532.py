#include "TNode.h"

TNode::TNode(ifstream* fin, bool needbracket)
{	
	left = 0;
	right = 0;
	char c;
	if (needbracket){
		*fin>>c;
		while (c!='('){
			*fin>>c;
		}
	}
	*fin>>weight;

	*fin>>c;
	while (c==' '){
		*fin>>c;
	}
	name="";		
	if ((c!=')')&&(c!='(')){
		name="";
		while ((c!=' ') && (c!='(') && (c!=')')){
			name=name+c;
			*fin>>c;
		}
	}
	if (c=='('){
		left = new TNode(fin, false);
		right = new TNode(fin, true);
		*fin>>c;
		while (c!=')'){
			*fin>>c;
		}
	}
}

TNode::~TNode(void)
{
}

/*
cat test.in | sed -e 's/))/) ) /g' | ./main
*/


#include <cstdio>
#include <string>
#include <vector>

using namespace std;

class Animal {
	public:
		vector<string> features;
		string name;
		
		Animal(string n);
		bool isFeatured(string f);
};

Animal::Animal(string n = "")
{
	name = n;
}

bool Animal::isFeatured(string f)
{
	for(int i=0;i<(int)features.size();i++)
		if (features[i] == f)
			return true;
	return false;
}

class Node {
	public:
		double weight;
		string name;
		Node *yes;
		Node *no;
		
		Node(double w, string n);
		double cuteness(Animal a);
		void dump(int off);
};

Node::Node(double w = 0.0, string n = "")
{
	weight = w;
	name = n;
	yes = NULL;
	no = NULL;
}

double Node::cuteness(Animal a)
{
	if (yes == NULL && no == NULL)
		return weight;
	
	if (a.isFeatured(name))
		return weight * yes->cuteness(a);
	return weight * no->cuteness(a);
}

void Node::dump(int off = 0)
{
	for(int i=0;i<off;i++)
		printf(" ");
	
	printf("%lf %s\n", weight, name.c_str());
	
	if (yes != NULL)
		yes->dump(off+1);
	if (no != NULL)
		no->dump(off+1);
}

void fillTree(Node *n)
{
	while(getchar() != '(');
	//getchar();
	
	double w;
	scanf("%lf", &w);
	//printf("c: %lf", w);
	
	char buf[512];
	scanf("%s", buf);
	
	if (string(buf) == ")")
		n->weight = w;
	else
	{
		n->weight = w;
		n->name = string(buf);
		
		n->yes = new Node;
		fillTree(n->yes);
		n->no = new Node;
		fillTree(n->no);
		while(getchar() != ')');
	}
}

Animal getAnimal(void)
{
	Animal buf;
	
	char name[512];
	int n;
	scanf("%s %d", name, &n);
	
	buf.name = string(name);
	
	for(int i=0;i<n;i++)
	{
		char f[512];
		scanf("%s", f);
		buf.features.push_back(string(f));
	}
	
	return buf;
}

int main(void)
{
	int n;
	scanf("%d", &n);
	
	for(int k=0;k<n;k++)
	{
		int trash;
		scanf("%d", &trash);
		
		Node root;
		fillTree(&root);
		
		int a;
		scanf("%d", &a);
		vector<Animal> animals;
		printf("Case #%d:\n", k+1);
		for(int i=0;i<a;i++)
			printf("%.7lf\n", root.cuteness(getAnimal()));
	}
	
	return 0;
}
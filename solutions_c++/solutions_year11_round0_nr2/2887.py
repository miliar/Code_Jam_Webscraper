#include <iostream>
#include <map>
#include <set>
#include <deque>

using namespace std;

typedef deque< char > SymQueue;
typedef pair< char, char > CharCouple;
typedef map< CharCouple, char > SymCombineMap;
typedef map< char, char > SymLinkMap;
typedef map< char, int > CountMap;

class SeenMap : public CountMap {
	public:
		SeenMap () : CountMap () {}

		void erase (char c) {
			CountMap::iterator it = find (c);
			if (it != end () && it->second > 0)
				--it->second;
		}

		void insert (char c) {
			CountMap::iterator it = find (c);
			if (it == end ())
				CountMap::insert (pair< char, int > (c, 1));
			else
				++it->second;
		}

		bool in (char c) {
			CountMap::iterator it = find (c);
			return it != end () && it->second > 0;
		}
};

class InvocQueue {
	private:
		SymQueue queue;
		
		SymLinkMap opposite;
		SeenMap seen;

		SymCombineMap combination;

	public:
		InvocQueue () {}

		void addCombination (char a, char b, char r) {
			combination[CharCouple (a, b)] = r;
			combination[CharCouple (b, a)] = r;
		}

		void addOpposite (char a, char b) {
			opposite[a] = b;
			opposite[b] = a;
		}

		void push (char toBePushed) {
			if (queue.size () > 0) {
				char prev = queue.back ();

				SymCombineMap::iterator it = combination.find (CharCouple (prev, toBePushed));
				if (it != combination.end ()) {
					seen.erase (prev);
					queue.back () = it->second;
				} else if (seen.in (opposite[toBePushed])) {
					seen.clear ();
					queue.clear ();
				} else {
					queue.push_back (toBePushed);
					seen.insert (toBePushed);
				}
			} else {
				queue.push_back (toBePushed);
				seen.insert (toBePushed);
			}
		}

		string get (void) {
			string res = "[";
			for (int i = 0; i < queue.size (); ++i) {
				res += queue[i];
				if (i < queue.size () - 1)
					res += ", ";
			}
			return res + "]";
		}
};

int main (void) {
	int n;
	
	cin >> n;
	for (int i = 0; i < n; ++i) {
		InvocQueue queue;
		int nbComb, nbOpp, nbChar;
		char a, b, c;
		
		cin >> nbComb;
		for (; nbComb > 0; --nbComb) {
			cin >> a >> b >> c;
			queue.addCombination (a, b, c);
		}
		
		cin >> nbOpp;
		for (; nbOpp > 0; --nbOpp) {
			cin >> a >> b;
			queue.addOpposite (a, b);
		}

		cin >> nbChar;
		for (; nbChar > 0; --nbChar) {
			cin >> a;
			queue.push (a);
		}

		cout << "Case #" << (i + 1) << ": " << queue.get () << endl;
	}

	return 0;
}

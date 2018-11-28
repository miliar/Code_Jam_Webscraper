#include <iostream>
#include <vector>

namespace CodeJam {
  namespace Magicka {
    typedef char Element;

    class Opposed {
    public:
      Opposed(): bitmap(0) {
      }

      void add(Element e) {
	int bit = e - 'A';

	bitmap |= (1 << bit);
      }

      void add(Opposed o) {
	bitmap |= o.bitmap;
      }

      void clear() {
	bitmap = 0;
      }

      bool contains(Element e) const {
	int bit = e - 'A';

	return bitmap & (1 << bit);
      }
      
    private:
      unsigned long bitmap;
    };

    class ElementRules {
    public:
      ElementRules(): opposed(1 << 8), combinations(1 << 16) {
      }

      void addCombineRule(Element a, Element b, Element result) {
	combinations[a + (b << 8)] = result;
	combinations[b + (a << 8)] = result;
      }

      void addOpposedRule(Element a, Element b) {
	opposed[a].add(b);
	opposed[b].add(a);
      }

      Opposed getOpposed(Element a) const {
	return opposed[a];
      }

      bool canCombine(Element a, Element b) const {
	return combinations[a + (b << 8)];
      }

      Element combine(Element a, Element b) const {
	return combinations[a + (b << 8)];
      }

    private:
      std::vector<Opposed> opposed;
      std::vector<Element> combinations;

      friend std::istream& operator>>(std::istream&, ElementRules&);
    };

    std::istream& operator>>(std::istream& is, ElementRules& rules) {
      std::string buf;
      int k;

      is >> k;
      for(int i = 0; i < k; i++) {
	is >> buf;
	rules.addCombineRule(buf[0], buf[1], buf[2]);
      }

      is >> k;
      for(int i = 0; i < k; i++) {
	is >> buf;
	rules.addOpposedRule(buf[0], buf[1]);
      }
    }

    class ElementSequence {
    public:
      ElementSequence(const ElementRules& rules): rules(rules) {
      }

      void add(Element e) {
	if(!elements.empty() && rules.canCombine(e, elements.back())) {
	  e = rules.combine(e, elements.back());
	  elements.pop_back();

	  resetOpposed();
	  
	  add(e);

	  return;
	}

	if(opposed.contains(e)) {
	  clear();

	  return;
	}

	elements.push_back(e);
	opposed.add(rules.getOpposed(e));
      }

    private:
      void resetOpposed() {
	opposed.clear();

	for(std::vector<Element>::iterator it = elements.begin(), end = elements.end(); it != end; ++it) {
	  opposed.add(rules.getOpposed(*it));
	}
      }

      void clear() {
	elements.clear();
	opposed.clear();
      }

      const ElementRules& rules;
      Opposed opposed;
      std::vector<Element> elements;

      friend std::ostream& operator<<(std::ostream&, const ElementSequence&);
    };

    std::ostream& operator<<(std::ostream& os, const ElementSequence& seq) {
      os << "[";

      for(int i = 0; i < seq.elements.size(); i++) {
	os << seq.elements[i] << (i == seq.elements.size() - 1 ? "" : ", ");
      }

      return os << "]";
    }

    void solveCase(int c) {
      ElementRules rules;
      int n; 
      std::string buf;

      std::cin >> rules ;
      std::cin >> n;
      std::cin >> buf;

      ElementSequence seq(rules);
      
      for(int i = 0; i < n; i++) {
	seq.add(buf[i]);
      }

      std::cout << "Case #" << c << ": " << seq << std::endl;
    }

    void solveAll() {
      int k; std::cin >> k;

      for(int i = 1; i <= k; i++) {
	solveCase(i);
      }
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  CodeJam::Magicka::solveAll();  

  return 0;
}

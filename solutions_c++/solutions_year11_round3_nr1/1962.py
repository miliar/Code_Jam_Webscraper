#include <vector>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

class SquareTiles {
  vector<string> m_lines;
  bool m_ok;
  vector<bool> m_closed;
public:
  SquareTiles(int r, int c) : m_ok(true) {
    m_lines.reserve(r);
    m_closed.reserve(c);
    for (int i = 0; i < c; ++i)
      m_closed.push_back(true);
  }

  void addLine(const string& line) {
    if (!m_ok)
      return;

    int countTiles = 0;
    for (int i = 0; i < line.size(); ++i) {
      if (line[i] == '#')
	++countTiles;
    }
    if (countTiles % 2 == 1) {
      m_ok = false;
      return;
    }

    m_lines.push_back(replaceToRed(line));
  }


  string replaceToRed(string line) {
    if (m_lines.empty()) {
      bool isOdd = true;
      for (int i = 0; i < line.size(); ++i) {
	if (line[i] == '#') {
	  if (isOdd) {
	    line[i] = '/';
	  } else {
	    line[i] = '\\';
	  }
	  m_closed[i] = false;
	  isOdd = !isOdd;
	}
      }
      return line;
    }

      string prev = m_lines.back();
      bool isOdd = true;
      for (int i = 0; i < line.size(); ++i) {
	if (line[i] == '#') {
	  if (m_closed[i]) {
	    if (isOdd) {
	      line[i] = '/';
	    } else {
	      line[i] = '\\';
	    }
	    m_closed[i] = false;
	  }
	  else {
	    if (isOdd) {
	      line[i] = '\\';
	    } else {
	      line[i] = '/';
	    }
	    m_closed[i] = true;
	  }
	  isOdd = !isOdd;
	}
	else {
	  if (!m_closed[i]) {
	    m_ok = false;
	    return line;
	  }
	}
      }	  
      return line;
  }

  bool closed(int c) {
    return m_closed[c];
  }

  string toRed() {
    if (!m_ok || !allClosed())
      return "Impossible\n";
    return toString();
  }

  bool allClosed() const {
    for (int i = 0; i < m_closed.size(); ++i)
      if (!m_closed[i])
	return false;
    return true;
  }

  string toString() {
    stringstream ss;
    for (int i = 0; i < m_lines.size(); ++i)
      ss << m_lines[i] << '\n';
    return ss.str();
  }
};

void squareTiles(istream& in, ostream& out) {
  int T;
  in >> T;
  for (int i = 0; i < T; ++i) {
    int R, C;
    in >> R >> C;
    SquareTiles s(R, C);
    for (int r = 0; r < R; ++r) {
      string str;
      in >> str;
      s.addLine(str);
    }
    out << "Case #" << (i + 1) << ":" << endl <<
      s.toRed();
  }
}

int main(int argc, char** argv) {
  squareTiles(cin, cout);
  return 0;
}

// This is written in vala, if you can't recognize the language

// This program makes use of glib functions
// http://ftp.acc.umu.se/pub/gnome/sources/glib/

const string uri = "A-large.in";

const string sample = "6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
";

enum rs {
    X_WON,
    O_WON,
	GAME_INCOMPLETE,
	DRAW;

    public string to_string() {
        switch (this) {
            case X_WON:
                return "X won";

            case O_WON:
                return "O won";

            case GAME_INCOMPLETE:
                return "Game has not completed";

            case DRAW:
                return "Draw";

            default:
                assert_not_reached();
        }
    }

	public static rs from_char (char c){
        switch (c) {
            case 'O':
                return rs.O_WON;

            case 'X':
                return rs.X_WON;

			case '.':
				return GAME_INCOMPLETE;

            default:
                assert_not_reached();
        }
	}
}

rs tictactoe (string[] s){
	//Horiz
	for (int i = 0; i < 4; i++){
		string str = s[i];
		char zero = str[0];
		if (zero == 'T'){
			zero = str[1];
		}
		for (int j = 0; j < 4; j++){
			if (str[j] == '.')
				break;
			if (zero != str[j] && str[j] != 'T')
				break;
			if (j == 3){
				return rs.from_char (zero);
			}
		}
	}

	//Vert
	for (int i = 0; i < 4; i++){
		char zero = s[0][i];
		if (zero == 'T'){
			zero = s[1][i];
		}
		for (int j = 0; j < 4; j++){
			if (s[j][i] == '.')
				break;
			if (zero != s[j][i] && s[j][i] != 'T')
				break;
			if (j == 3){
				return rs.from_char (zero);
			}
		}
	}

	//Diagonal \
	{
		char zero = s[0][0];
		if (zero == 'T'){
			zero = s[1][1];
		}
		for (int j = 0; j < 4; j++){
			if (s[j][j] == '.')
				break;
			if (zero != s[j][j] && s[j][j] != 'T')
				break;
			if (j == 3){
				return rs.from_char (zero);
			}
		}
	}

	//Diagonal /
	{
		char zero = s[0][3-0];
		if (zero == 'T'){
			zero = s[1][3-1];
		}
		for (int j = 0; j < 4; j++){
			if (s[j][3-j] == '.')
				break;
			if (zero != s[j][3-j] && s[j][3-j] != 'T')
				break;
			if (j == 3){
				return rs.from_char (zero);
			}
		}
	}

	// No wins. Is it over?

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (s[i][j] == '.')
				return rs.GAME_INCOMPLETE;
		}
	}

	return rs.DRAW;
}

void run (DataInputStream d, FileStream o) {
	int numlines = int.parse (d.read_line ());
	for (int i = 0; i < numlines; i++){
		string[] strs = new string[4];

		for (int j = 0; j < 4; j++){
			strs[j] = d.read_line ();
		}
		d.read_line ();

		rs res = tictactoe(strs);

		o.printf("Case #%i: %s\n", i + 1, res.to_string ());
	}
}

int main () {
	if (uri == ""){
		// testing
		var input = new MemoryInputStream.from_data (sample.data, null);
		var d = new DataInputStream (input);
		run (d, stdout);
	} else {
		// run
		var o = FileStream.open ("./" + Log.FILE + ".res", "w");
		var input = File.new_for_path (uri);
		var d = new DataInputStream (input.read ());
		run (d, o);
	}
	return 0;
}

package aprokh.gcj2017q


import java.util.ArrayList
import java.util.StringTokenizer
//import scala.reflect.io.File
import java.io.BufferedReader
import java.io.BufferedInputStream
import java.io.InputStreamReader
import java.io.ByteArrayInputStream
import java.io.InputStream

object GCJ2017_A_a {   var br = createBufferedReader(); var debugV = false 
    
    //COMMENT ME !
//    runTest(Test.gen1)
//    debugV = true
//    file = File("C:\\temp\\google cj\\2014q\\c-small.res")
  
  def invert(ss: Array[Char], ind: Int, len: Int): Array[Char] = {
    val res = (0 until ss.size).map( x => {
      if (x >= ind && x < ind + len) {
        if (ss(x) == '-') '+' else '-'                
      } else ss(x)
    })
    res.toArray
  }

  def main(args: Array[String]): Unit = {
    //---------------------------- parameters reading 
    val cases = readLine.int
    
    for (i <- 1 to cases) {
      val pars = readLine.fullLine.split(" ")
      var str = pars(0).toArray
      val num = pars(1).toInt
      
      
      
      var ind = str.indexOf('-')
      var count = 0
      while (ind > -1 && ind <= str.length() - num) {
        str = invert(str, ind, num)
        ind = str.indexOf('-')
        count += 1
      }
      
      val res = if (ind == -1) { 
        count+""        
      } else "IMPOSSIBLE" 
      outLn(s"Case #$i: $res")
    }
    
    finish
  }
  
  
  //============================ service code ======================

//  var file:File = null
  val resultStr = new StringBuilder
  def outLn(str:String) = resultStr.append(str).append("\n")
  def outLn(number:Integer) = resultStr.append(number+"").append("\n")
  def finish() {
//    if (file == null || !devEnv) {
      println(resultStr.toString())
//    } else {
//      file.writeAll(resultStr.toString())
//    }
  }
  
  def readLine() = new Line  
  class Line {
    val fullLine = br.readLine()
    val tok = new StringTokenizer(fullLine, " ")
    def int = tok.nextToken().toInt
    def long = tok.nextToken().toLong
    def double = tok.nextToken().toDouble
    def string = tok.nextToken()
  }
  
  def createBufferedReader(inst:InputStream = System.in): BufferedReader = {
    val bis = if (inst == null) new BufferedInputStream(System.in) else new BufferedInputStream(inst);
    new BufferedReader(new InputStreamReader(bis));
  }
  
  def runTest(str:String) = if (devEnv) { 
    br = createBufferedReader(new ByteArrayInputStream(str.trim.getBytes("ISO-8859-1")))
  }
  
  def debug(x: => String) = if (debugV && devEnv) println(x) // nullary function
  
  lazy val devEnv = this.getClass.getCanonicalName.contains(".")
  
//============================================================================================
object Test {
  
val sa1 = """
3
---+-++- 3
+++++ 4
-+-+- 4
"""

val sa2 = """
1
-+-+- 3
"""

val sa3 = """
"""

val large = s"""
1
"""+ ("-+-+-+-+-+" * 100) + "- 3"

val gen1 = """
5
+---------++-------++++--+++++--+--+-++++---+-++---+----------+++++++++-+-------++-++++++++---+--++++++++---++++-+----++++-+-++++--++-+-++++++---++--+++++---+++-----++++-------++---------++------+++----++++-++-+-------+++-+----++--++++++-++--+++---++ 11
+++--------++++++++++++++++--+++++-++-++++----+++++++--++---+--+++++--------+++++---+++++-+------+-++++++++++-+-----+-+-----++++++++++++--+--+++--+-+-++++++--++-----+++-++++----++++--------+++------+-++++++-+++------++------++--------++------++-----+-------+--+++++---+----+---++++--++----+-++-++++--+-++++++---++++++--++++++++++++++++++++++++++++--++++++--+++++++----------------++++++++++++++++++ 8
++++++++++++++++++---------------++++++++++++++++++++++++++++++++---------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--+++++++++++++--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 15
+++++++++++++++--------------------+++++++++++++++++++++++++++++++++++++++--------------------++++++++++++++++++++++++++++--++++++++++++++++++--++++++++++++++++++++++++-------------+++++++-------------++++++++++++++++++++++++--------------------+++++++++++++++--------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--------------------+--------------------++----------++++++++++----------+++++++++++++++++++++++++++++++++++++++++++++ 20
++++++++++++++++++++++++++++++++++++++++++++++-------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-------++++++++++++++++-------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 7
"""
//59, 62, 7, 12, 4

}

}


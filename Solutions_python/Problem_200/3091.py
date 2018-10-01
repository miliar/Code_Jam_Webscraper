import java.io.File

import scala.annotation.tailrec
import scala.io.Source

val filePath = "/Users/user/Work/Projects/CodeJam2017/src/main/scala/B-large.in"
val source = Source.fromFile(new File(filePath))
val lines = source.getLines()



for (i <- 1 to lines.next().toInt) {

  val n = lines.next()

  @tailrec
  def solve(n: String, head: String = "", tail: String = ""): String = {
    if (n.length == 1) head + n + tail
    else {
      val h = n.head
      if (n.tail.forall(_ >= h)) solve(n.tail, head + n.head, tail)
      else {
        val i = n.indexWhere(_ < h)
        solve(n.substring(0, i - 1) + (n(i - 1) - 1).toChar, head,
          Seq.fill(n.length - i)('9').mkString + tail)
      }
    }
  }

  val res = solve(n)
  println(s"Case #$i: ${if (res.startsWith("0")) res.tail else res}")
}
